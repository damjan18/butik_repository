from db import connect
from datetime import datetime

def prodaj_proizvod(product_id, quantity_sold, date):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT quantity, selling_price FROM products WHERE id = ?", (product_id,))
    result = cursor.fetchone()
    if not result:
        print("Proizvod ne postoji.")
        return
    current_quantity, selling_price = result
    
    if quantity_sold > current_quantity:
        print("Nema dovoljno zaliha.")
        return
    
    total_price = quantity_sold * selling_price
    new_quantity = current_quantity - quantity_sold
    
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    cursor.execute("INSERT INTO sales (product_id, date, quantity_sold, total_price) VALUES (?, ?, ?, ?)",(product_id, date, quantity_sold, total_price))
    
    conn.commit()
    conn.close()
    
def prodaj_proizvod_interaktivno():
    product_id = int(input("ID Proizvoda: "))
    quantity = int(input("Kolicina za prodaju: "))
    date = datetime.now().strftime("%Y-%m-%d")
    prodaj_proizvod(product_id, quantity, date)
    