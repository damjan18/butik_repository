import sqlite3
def connect():
    return sqlite3.connect("butik.db")


# Kreiranje tabele
def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        size TEXT,
        quantity INTEGER,
        purchase_price REAL,
        selling_price REAL
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,\
        product_id INTEGER,
        date TEXT,
        quantity_sold INTEGER,
        total_price REAL,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )               
    """)

    conn.commit()
    conn.close()
    
init_db()