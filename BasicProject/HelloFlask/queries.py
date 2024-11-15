import psycopg2
from psycopg2 import sql

class Queries:
    def __init__(self):
        # Initialize the connection to the database
        self.conn = psycopg2.connect(
            dbname="TestDB",
            user="postgres",
            password="#aH6TR5fkcdx99",
            host="localhost",
            port="5432"
        )
        self.cursor = self.conn.cursor()


    def close(self):
        # Close the database connection
        self.cursor.close()
        self.conn.close()

    # Example query methods
    def insert_item(self, item_name, item_description, date_lost, buildingCode):
        query = """
            INSERT INTO items (itemName, itemDescription, dateLost, buildingCode)
            VALUES (%s, %s, %s, %s)
        """
        # Use parameterized queries to prevent SQL injection
        self.cursor.execute(query, (item_name, item_description, date_lost, buildingCode))
        self.conn.commit()  # Commit the transaction to save the changes

    def get_items_by_building_code(self, building_code):
        """Fetch all items associated with a specific building code."""
        self.cursor.execute("""
            SELECT items.*
            FROM items
            JOIN building ON items.buildingCode = building.buildingCode
            WHERE building.buildingCode = %s
        """, (building_code,))
        return self.cursor.fetchall()  # Fetch all matching items

    def createBuilding(self, buildingCode):
        query = """
            INSERT INTO building(buildingCode)
            VALUES (%s)
        """
        self.cursor.execute(query, (buildingCode,))
        self.conn.commit()

    def createAccount(self, username, password, email):
        query = """
            INSERT INTO users (username, password, email)
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (username, password, email))
        self.conn.commit()

    def getUser(self, username, email):
        self.cursor.execute("""
        SELECT id, username, password 
        FROM users 
        WHERE username = %s OR email = %s
        """, (username, email))
        row = self.cursor.fetchone()
        if row:
            return {"id": row[0], "username": row[1], "password": row[2]}  # Convert to dictionary
        return None






# Close the connection when done