'''
2. Tworzenie klasy
'''



class Receipt:
    name = "Ciasto kruche"
    ingredients = ["mąka", "jajka", "masło", "cukier puder", "sól"]
    price = 5
    time = 60


# obiekt_klasy = Receipt()
# print(obiekt_klasy.name)
# print(obiekt_klasy.ingredients)
# print(obiekt_klasy.price)
# print(obiekt_klasy.time)


# Zmiana wartości atrybutu
# obiekt_klasy.price = 10
# print(obiekt_klasy.price)


class Kalkulator:
    def dodawanie(self, a, b): 
        return a + b

    def odejmowanie(self, a, b):
        return a - b

    def mnozenie(self, a, b):
        return a * b

    def dzielenie(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Nie można dzielić przez zero"


# kalk = Kalkulator()
# print("Dodawanie:", kalk.dodawanie(5, 3))
# print("Odejmowanie:", kalk.odejmowanie(5, 3))
# print("Mnożenie:", kalk.mnozenie(5, 3))
# print("Dzielenie:", kalk.dzielenie(5, 3))


class Prostokat:
    def __init__(self, dlugosc=20, szerokosc=30):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def obwod(self):
        return 2 * (self.dlugosc + self.szerokosc)

    def pole(self):
        return self.dlugosc * self.szerokosc


# prostokat = Prostokat(4, 6)
# print("Obwód prostokąta:", prostokat.obwod())
# print("Pole prostokąta:", prostokat.pole())


class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def informacje(self):
        return f"Tytuł: {self.tytul}, Autor: {self.autor}, Rok wydania: {self.rok_wydania}"


# ksiazka = Ksiazka("Władca Pierścieni", "J.R.R. Tolkien", 1954)
# print("Informacje o książce:", ksiazka.informacje())


'''
Rodzaje metod
'''

# Metoda instancji
class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.przebieg = 0

    def jedz(self, dystans):
        self.przebieg += dystans
        print(f"Przejechano {dystans} km. Aktualny przebieg: {self.przebieg} km.")

# Utworzenie instancji klasy
# moj_samochod = Samochod("Toyota", "Corolla")
#Wywołanie metody instancji
# moj_samochod.jedz(50)


# Metoda statyczna
class Kalkulator:
    @staticmethod
    def dodaj(a, b):
        return a + b

# Wywołanie metody statycznej
# wynik = Kalkulator.dodaj(5, 3)
# print("Wynik dodawania:", wynik)


# Metoda klasy
class KontoBankowe:
    liczba_kont = 0

    def __init__(self, saldo):
        self.saldo = saldo
        KontoBankowe.liczba_kont += 1

    @classmethod
    def ile_kont(cls):
        return cls.liczba_kont

# Utworzenie instancji klasy
# konto1 = KontoBankowe(1000)
# konto2 = KontoBankowe(2000)
# konto3 = KontoBankowe(3000)

# Wywołanie metody klasy
# print("Liczba utworzonych kont:", KontoBankowe.ile_kont())
