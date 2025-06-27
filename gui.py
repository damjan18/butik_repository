import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog, ttk
from products import dodaj_proizvod, prikazi_proizvode
from sales import prodaj_proizvod
from report import prikazi_izvjestaj
from datetime import datetime

def gui_dodaj_proizvod():
    def submit():
        try:
            dodaj_proizvod(
                name_entry.get(),
                category_entry.get(),
                size_entry.get(),
                int(quantity_entry.get()),
                float(purchase_price_entry.get()),
                float(selling_price_entry.get())
            )
            messagebox.showinfo("Uspjeh", "Proizvod dodat")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Greska", str(e))
    
    window = tk.Toplevel(root)
    window.title("Dodaj proizvod")
    
    tk.Label(window, text="Naziv").grid(row=0, column=0)
    tk.Label(window, text="Kategorija").grid(row=1, column=0)
    tk.Label(window, text="Velicina").grid(row=2, column=0)
    tk.Label(window, text="Kolicina").grid(row=3, column=0)
    tk.Label(window, text="Nabavna cjena").grid(row=4, column=0)
    tk.Label(window, text="Prodajna cjena").grid(row=5, column=0)
    
    name_entry = tk.Entry(window)
    category_entry = tk.Entry(window)
    size_entry = tk.Entry(window)
    quantity_entry = tk.Entry(window)
    purchase_price_entry = tk.Entry(window)
    selling_price_entry = tk.Entry(window)
    
    
    name_entry.grid(row=0, column=1)
    category_entry.grid(row=1, column=1)
    size_entry.grid(row=2, column=1)
    quantity_entry.grid(row=3, column=1)
    purchase_price_entry.grid(row=4, column=1)
    selling_price_entry.grid(row=5, column=1)
    
    tk.Button(window, text="Dodaj", command=submit).grid(row=6, column=0, columnspan=2)
    
def gui_prikazi_proizvode():
    window = tk.Toplevel(root)
    window.title("Svi proizvodi")
    
    tree = ttk.Treeview(window, columns=("ID", "Naziv", "Kategorija", "Velicina", "Kolicina", "Cena"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    conn = __import__("db").connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, size, quantity, selling_price FROM products")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()
    
    tree.pack(expand=True, fill="both")
    
def gui_prodaj_proizvod():
    product_id = simpledialog.askinteger("Prodaja", "Unesi ID proizvoda:")
    kolicina = simpledialog.askinteger("Prodaja", "Unesi kolicinu:")
    if product_id and kolicina:
        prodaj_proizvod(product_id, kolicina, datetime.now().strftime("%Y-%m-%d"))
        messagebox.showinfo("Uspjeh", "Prodaja zabiljezena.")
        
        
def gui_izvjestaj():
    prikazi_izvjestaj()
    

root = tk.Tk()
root.title("Evidencija Butika")

tk.Button(root, text="Dodaj proizvod", width=30, command=gui_dodaj_proizvod).pack(pady=5)
tk.Button(root, text="Prikazi proizvode", width=30, command=gui_prikazi_proizvode).pack(pady=5)
tk.Button(root, text="Prodaj proizvod", width=30, command=gui_prodaj_proizvod).pack(pady=5)
tk.Button(root, text="Izvjestaj o prodaji", width=30, command=gui_izvjestaj).pack(pady=5)

root.mainloop()