'''
4. Konstruktor klasy w Pythonie
'''

class Person:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    
    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

# Tworzenie instancji klasy Osoba i automatyczne wywołanie konstruktora
# osoba1 = Person("Jan", "Kowalski")

# Wyświetlanie atrybutów obiektu
# print(osoba1.imie)
# print(osoba1.nazwisko)
# print(osoba1.przedstaw_sie())


# Przykład 1
class Receipt:
    # Atrybuty klasy
    name = "Nazwa"
    ingredients = ["składnik 1", "składnik 2", "składnik 3"]
    price = 0
    time = 0

    def __init__(self, name, ingredients, price, time):
        # Atrybuty instancji klasy
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.time = time

    def print_info(self):
        print(f"Nazwa: {self.name}")
        print(f"Składniki: {self.ingredients}")
        print(f"Cena: {self.price}")
        print(f"Czas przygotowania: {self.time}")


# obiekt_klasy = Receipt("Ciasto kruche", ["mąka", "jajka", "masło", "cukier puder", "sól"], 5, 60)
# obiekt_klasy.print_info()


# Przykład 2
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# human1 = Human("John", 20)
# human1.say_hello()
# human2 = Human("Kate", 25)
# human2.say_hello()

# super()
class ParentClass:
    def __init__(self, imie):
        self.imie = imie

class ChildClass(ParentClass):
    def __init__(self, imie, wiek):
        super().__init__(imie) # super jest użyte w celu wywołania konstruktora klasy nadrzędnej (rodzica) i przekazania do niego argumentów imie i wiek
        self.wiek = wiek

# Przykład użycia:
dziecko = ChildClass("Jan", 10)
print(dziecko.imie)  # Dostęp do atrybutu z klasy nadrzędnej
print(dziecko.wiek)  # Atrybut specyficzny dla klasy Dziecko