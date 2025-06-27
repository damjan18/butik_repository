from db import connect
def dodaj_proizvod(name, category, size, quantity, purchase_price, selling_price):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO products (name, category, size, quantity, purchase_price, selling_price)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, category, size, quantity, purchase_price, selling_price))
    conn.commit()
    conn.close()
    
    
def dodaj_proizvod_interaktivno():
    name = input("Naziv: ")
    category = input("Kategorija: ")
    size = int(input("Velicina: "))
    quantity = int(input("Kolicina: "))
    purchase_price = float(input("Nabavna cjena: "))
    selling_price = float(input("Prodajna cjena: "))
    
    dodaj_proizvod(name, category, size, quantity, purchase_price, selling_price)
    
    
def prikazi_proizvode():
    conn = connect()
    cursor = conn.cursor()
    for row in cursor.execute("SELECT * FROM products"):
        print(row)
    conn.close()
    
    
    
    
    