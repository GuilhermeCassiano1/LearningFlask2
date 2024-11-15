import psycopg2
from psycopg2 import sql

def connect_db():
    conn = psycopg2.connect(
        dbname="TestDB",
        user="postgres",
        password="#aH6TR5fkcdx99",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    return conn

def apply_changes():
    conn = connect_db()
    cursor = conn.cursor()

    # 2024-11-12: Added locationFound column and buildingCode foreign key to items
    """
    ALTER TABLE items
    ADD COLUMN IF NOT EXISTS buildingCode VARCHAR(50) REFERENCES building(buildingCode);
    """
    # 2024-11-14: Added item type and brand (optional) columns for the Item table and removed "Item name" column
    """
    ALTER TABLE items
    ADD COLUMN IF NOT EXISTS itemType VARCHAR(50);
    """
    """
    ALTER TABLE items
    ADD COLUMN IF NOT EXISTS brand VARCHAR(50) NULL;
    """
    """
    ALTER TABLE items
    DROP COLUMN itemName;
    """
    # Execute the SQL to apply the change
    cursor.execute("""
    """)
    
    # Commit changes and close
    conn.commit()
    cursor.close()
    conn.close()
    print("Database changes applied successfully.")

if __name__ == "__main__":
    apply_changes()
