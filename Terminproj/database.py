import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host="10.2.2.29", 
            user="Aerol",
            password="Anmea050*",
            database="Cartdata",
            port=3306
        )
        if connection.is_connected():
            print("Connection successful!")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

