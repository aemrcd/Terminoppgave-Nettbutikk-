import uuid  
from flask import Flask, render_template, request, redirect, url_for, session ,flash
from database import connect_to_database
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'Frendon&Angelito'

# Home

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/Cart')
def Cart():
    # Retrieve the cart from the session
    cart = session.get('cart', [])
    
    # Calculate total price
    total_price = 0
    for item in cart:
        total_price += float(item['price']) * item['quantity']
    
    # Render the cart page with the total price
    return render_template('cart.html', cart=cart, total_price=total_price)


# Helper function to initialize cart
def initialize_cart():
    if 'cart' not in session:
        session['cart'] = []
    if 'purchase_history' not in session:
        session['purchase_history'] = []  

# Add product to the cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Initialize the cart 
    if 'cart' not in session:
        session['cart'] = []
    
    
    # get  product data from the form
    product_id = request.form.get('product_id')
    product_name = request.form.get('product_name')
    product_price = request.form.get('product_price')
    quantity = int(request.form.get('quantity', 1))  
    image = request.form.get('product_image')

    # Validate inputs
    if not all([product_id, product_name, product_price]):
        return redirect(url_for('Home'))  
    
    # Check if the product already exists in the cart
    item_exists = False
    for item in session['cart']:
        if item['id'] == product_id:  
            item['quantity'] += quantity  
            item_exists = True
            break

    # If item doesn't exist in the cart, add it as a new item
    if not item_exists:
        session['cart'].append({
            'uuid': str(uuid.uuid4()),  
            'id': product_id,
            'name': product_name,
            'price': product_price,
            'quantity': quantity,  
            'image': image
        })

    session.modified = True  

    return redirect(url_for('Cart'))

@app.route('/update_quantity/<uuid>', methods=['POST'])
def update_quantity(uuid):
    cart_items = session.get('cart', [])
    for item in cart_items:
        if str(item['uuid']) == uuid:  # Convert to string for comparison
            action = request.form.get('action')

            # Update the quantity based on the action
            if action == 'increase':
                item['quantity'] += 1
            elif action == 'decrease' and item['quantity'] > 1:
                item['quantity'] -= 1
            break  # Exit loop once item is found and updated

    # Save the updated cart back to the session
    session['cart'] = cart_items
    session.modified = True  # Ensure Flask saves the session changes

    return redirect(url_for('Cart'))


# Remove item from the cart using unique UUID
@app.route('/remove_from_cart/<uuid>', methods=['POST'])
def remove_from_cart(uuid):
    initialize_cart()
    # Remove only the item with the matching UUID
    session['cart'] = [item for item in session['cart'] if item['uuid'] != uuid]
    session.modified = True  
    return redirect(url_for('Cart'))

@app.route('/checkout', methods=['POST'])
def checkout():
    initialize_cart()  
    if session['cart']:
        # Create the purchase entry
        purchase_entry = {
            'date': datetime.now().strftime("%Y-%m-%d"),
            'items': session['cart'].copy() 
        }
        connection = connect_to_database()
        if connection is None:
            return "❌ Failed to connect to the database.", 500
        
        total_price = sum(float(item['price']) * item['quantity'] for item in session['cart'])

        cursor = connection.cursor()
        
        # Insert into 'purchases' table
        cursor.execute("""
            INSERT INTO purchases (cart_id, total_price) VALUES (%s, %s)
        """, (str(uuid.uuid4()), total_price))  
        connection.commit()
        
        purchase_id = cursor.lastrowid  # Get last inserted purchase id
        
        # Insert purchase items
        for item in session['cart']:
            product_id = int(item['id'])
            cursor.execute("""
                INSERT INTO purchase_items (purchase_id, product_id, product_name, product_price, quantity, image) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (purchase_id, product_id, item['name'], item['price'], item['quantity'], item['image']))
        
        connection.commit()
        connection.close()
        
        
        # Append to purchase history in session
        session['purchase_history'].append(purchase_entry)
        
        flash('Purchase successful! Thank you for your order.', 'success')
        
        # Clear the cart after purchase
        session['cart'] = []
        session.modified = True 

    return redirect(url_for('Cart'))

@app.route('/purchase_history')
def purchase_history():
    # Ensure session has purchase history
    initialize_cart()  

    # Connect to the database
    connection = connect_to_database()
    if connection is None:
        return "❌ Failed to connect to the database.", 500
    
    cursor = connection.cursor()
    
    # Retrieve all purchases from the database
    cursor.execute("SELECT * FROM purchases")
    db_purchases = cursor.fetchall()
    
    # Create a list to hold the updated purchases as dictionaries
    updated_purchases = []
    
    # Get items related to each purchase from the database
    for purchase in db_purchases:
        purchase_id = purchase[0]  # Assuming 'id' is the first column
        
        # Fetch the items for the current purchase
        cursor.execute("""
            SELECT * FROM purchase_items WHERE purchase_id = %s
        """, (purchase_id,))
        purchase_items = cursor.fetchall()

        # Create a new dictionary for each purchase
        purchase_dict = {
            'id': purchase[0],  # Assuming 'id' is the first column
            'date': datetime.strftime(purchase[2], '%Y-%m-%d'),  # Assuming 'purchase_date' is the 3rd column (timestamp)
            'total_price': purchase[3],  # The total price of the purchase
            'items': []  # Will be populated below
        }
        
        # Add the items to the purchase_dict
        for item in purchase_items:
            try:
                price = float(item[4]) if item[4] else 0.0  # product_price is the 5th column
                quantity = item[5]  # quantity is the 6th column
                product_name = item[3]  # product_name is the 4th column
                image = item[6]  # image is the 7th column

                purchase_dict['items'].append({
                    'name': product_name,
                    'price': price,
                    'quantity': quantity,
                    'image': image
                })
            except ValueError as e:
                print(f"Error processing item: {item} - {e}")
                continue
        
        updated_purchases.append(purchase_dict)
    
    # Calculate the grand total of all purchases
    grand_total = 0
    for purchase in updated_purchases:
        item_total = sum(float(item['price']) * item['quantity'] for item in purchase['items'])
        purchase['total'] = round(item_total, 2)  # Store total for this purchase
        grand_total += item_total
    
    connection.close()
    
    # Render the template with updated purchase history data
    return render_template('mineordre.html', purchases=updated_purchases, grand_total=round(grand_total, 2))






# MORE INFORMATION BUTTON LINKS

@app.route('/xboxkontroller')
def xboxkontroller():
    return render_template('xboxkontroller.html')
@app.route('/tklkeyboard')
def tklkeyboard():
    return render_template('tklkeyboard.html')
@app.route('/razerkeyboard')
def razerkeyboard():
    return render_template('razerkeyboard.html')
@app.route('/ps5kontroller')
def ps5kontroller():
    return render_template('ps5kontroller.html')
@app.route('/ps4kontroller')
def ps4kontroller():
    return render_template('ps4kontroller.html')
@app.route('/60keyboard')
def gamingkeyboard():
    return render_template('60keyboard.html')


if __name__ == '__main__':
    app.run(debug=True)
