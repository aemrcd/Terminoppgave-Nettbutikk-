import mysql.connector
from mysql.connector import Error


def connect_to_database():
    # """Connect to the cartdata database and return the connection object."""
    try:
        # connection = mysql.connector.connect(
        #     host="localhost", 
        #     user="root",
        #     password="",
        #     database="cartdata",
        #     port=3306
        connection = mysql.connector.connect(
        host="10.2.2.29", 
        user="Aerol",
        password="Anmea050*",
        database="Cartdata",
        port=3306
        )
        if connection.is_connected():
            print("✅ Connection successful!")
            return connection
    except Error as e:
        print(f"❌ Error: {e}")
        return None

def create_tables(connection):
    # """Create the purchases and purchase_items tables in the cartdata database."""
    try:
        cursor = connection.cursor()
        
        # SQL to create purchases table
        create_purchases_table = """
        CREATE TABLE IF NOT EXISTS purchases (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cart_id VARCHAR(255) NOT NULL, 
            purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
            total_price DECIMAL(10, 2) NOT NULL
        );
        """
        
        # SQL to create purchase_items table
        create_purchase_items_table = """
        CREATE TABLE IF NOT EXISTS purchase_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            purchase_id INT NOT NULL, 
            product_id VARCHAR(255) NOT NULL, 
            product_name VARCHAR(255) NOT NULL, 
            product_price DECIMAL(10, 2) NOT NULL, 
            quantity INT NOT NULL, 
            image VARCHAR(255), 
            FOREIGN KEY (purchase_id) REFERENCES purchases (id) ON DELETE CASCADE
        );
        """
        
        # Execute the table creation queries
        cursor.execute(create_purchases_table)
        cursor.execute(create_purchase_items_table)
        
        print("✅ Tables 'purchases' and 'purchase_items' created successfully.")
    except Error as e:
        print(f"❌ Error creating tables: {e}")

# Main program execution
connection = connect_to_database()

if connection is not None and connection.is_connected():
    create_tables(connection)  # Create the tables inside the 'cartdata' database
    connection.close()         # Close the connection
    print("✅ Connection closed.")
else:
    print("❌ Failed to connect to the database.")













# def connect_to_database():
#     try:
#         # Establish connection
# # connection = mysql.connector.connect(
# #     host="10.2.2.29", 
# #     user="Aerol",
# #     password="Anmea050*",
# #     database="Cartdata",
# #     port=3306
# # )