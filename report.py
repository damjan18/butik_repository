import pandas as pd
from db import connect


def prikazi_izvjestaj():
    conn = connect()
    df = pd.read_sql_query("""
        SELECT s.id, p.name, s.date, s.quantity_sold, s.total_price
        FROM sales s
        JOIN products p ON s.product_id = p.id                   
    """, conn)
    
    conn.close()
    print(df)
    print("Ukupna zarada:", df["total_price"].sum())