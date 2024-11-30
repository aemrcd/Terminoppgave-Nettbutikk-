import uuid  # Import for generating unique IDs
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Frendon&Angelito'

# Helper function to initialize cart
def initialize_cart():
    if 'cart' not in session:
        session['cart'] = []

# Hjemmeside
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
    return render_template('mineordre.html')  # Redirect to a checkout page or continue processing

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
    quantity = int(request.form.get('quantity', 1))  # Get quantity from the form (default to 1)
    image = request.form.get('product_image')

    # Validate inputs
    if not all([product_id, product_name, product_price]):
        return redirect(url_for('Home'))  # Redirect to home with an error message
    
    # Check if the product already exists in the cart
    item_exists = False
    for item in session['cart']:
        if item['id'] == product_id:  # Check if the product is already in the cart
            item['quantity'] += quantity  # Increase the quantity by the amount specified
            item_exists = True
            break

    # If item doesn't exist in the cart, add it as a new item
    if not item_exists:
        session['cart'].append({
            'uuid': str(uuid.uuid4()),  # Generate a unique ID
            'id': product_id,
            'name': product_name,
            'price': product_price,
            'quantity': quantity,  # Set the specified quantity
            'image': image
        })

    session.modified = True  # Ensure Flask saves the session changes

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



if __name__ == '__main__':
    app.run(debug=True)
