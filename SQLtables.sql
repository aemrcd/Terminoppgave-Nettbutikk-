CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id TEXT NOT NULL, -- Links the purchase to the session/cart
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    total_price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS purchase_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_id INTEGER NOT NULL, Foreign key linking to purchases
    product_id TEXT NOT NULL, 
    product_name TEXT NOT NULL, 
    product_price REAL NOT NULL, 
    quantity INTEGER NOT NULL, 
    image TEXT, 
    FOREIGN KEY (purchase_id) REFERENCES purchases (id) ON DELETE CASCADE
);
