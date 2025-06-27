from products import dodaj_proizvod_interaktivno, prikazi_proizvode
from sales import prodaj_proizvod_interaktivno
from report import prikazi_izvjestaj


def meni():
    while True:
        print("\n--- BUTIK MENI ---")
        print("1. Dodaj novi proizvod")
        print("2. Prikazi sve proizvode")
        print("3. Prodaj proizvod")
        print("4. Izvjestaj o prodaju")
        print("5. Izlaz")
        
        izbor = int(input("Izaberi opciju: "))
        
        if izbor == 1:
            dodaj_proizvod_interaktivno()
        elif izbor == 2:
            prikazi_proizvode()
        elif izbor == 3:
            prodaj_proizvod_interaktivno()
        elif izbor == 4:
            prikazi_izvjestaj()
        elif izbor == 5:
            print("Adio dondo Pero")
            break
        else:
            print("Falio si broj")
            

if __name__ == "__main__":
    meni()