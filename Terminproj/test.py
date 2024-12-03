import uuid  
from flask import Flask, render_template, request, redirect, url_for, session
from database import mydb

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

@app.route('/checkout', methods=['POST'])
def checkout():
    # Handle the payment process here 
    return render_template('mineordre.html') 

# Helper function to initialize cart
def initialize_cart():
    if 'cart' not in session:
        session['cart'] = []


# Add product to the cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Initialize the cart if not already initialized
    if 'cart' not in session:
        session['cart'] = []
    
    
    # Retrieve product data from the form
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

    # Ensure UUID comparison is consistent
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
    session.modified = True  # Mark session as modified
    return redirect(url_for('Cart'))

# Order Section
@app.route('/Orders')
def Orders():
    return render_template('mineordre.html')

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

@app.route('/purchase_history')
def purchase_history():
    return render_template('mineordre.html')


if __name__ == '__main__':
    app.run(debug=True)
