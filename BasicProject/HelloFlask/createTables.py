import psycopg2
from psycopg2 import sql

def create_tables():
    # Connect to the 'TestDB' database
    conn = psycopg2.connect(
        dbname="TestDB",
        user="postgres",
        password="#aH6TR5fkcdx99",
        host="localhost",
        port="5432"
    )
    
    # Create a cursor object
    cursor = conn.cursor()

    # 2024-11-12: Created Items and Building tables

    """
    CREATE TABLE IF NOT EXISTS building (
    buildingCode VARCHAR(50) PRIMARY KEY
    );
    """
    """
    CREATE TABLE IF NOT EXISTS items (
    itemName VARCHAR(50),
    itemDescription VARCHAR(100),
    dateLost DATE,
    PRIMARY KEY (itemName, dateLost)
    );
    """

    # 2024-14-11 Created users Table

    """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        email TEXT UNIQUE NOT NULL, 
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
    """

    # Define SQL queries for creating tables
    create_table_queries = []

    # Execute each query to create tables
    for query in create_table_queries:
        cursor.execute(query)
    
    # Commit changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()
