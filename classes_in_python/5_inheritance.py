'''
5 . Dziedziczenie  - ponowne użycie klasy na podstawie innej klasy 
'''

# Przykład 1
class Animal:
    def ruch(self):
        print("Zwierze porusza się")

class Bird(Animal):
    def latanie(self):
        print("Ptak fruwa")

class Mammal(Animal):
    def karmienie(self):
        print("Ssak karmi się mlekiem")

# Przykłady dziedziczenia:
# orzel = Bird()
# orzel.ruch()  # Odziedziczone od Zwierze
# orzel.latanie()  # Odziedziczone od Ptak

# kot = Mammal()
# kot.ruch()  # Odziedziczone od Zwierze
# kot.karmienie()  # Odziedziczone od Ssak


# Metoda Resolution Order (MRO)
# print(Bird.__mro__)  # lub Bird.mro()

# Przykład 2

class ProgrammingLanguage:
   def __init__(self, name, typing, level):
       self.name = name
       self.typing = typing
       self.level = level
 
   def __str__(self):
       return f"{self.name}, {self.typing}, {self.level}"


class Python(ProgrammingLanguage):
    def __init__(self, name="Python", typing="Dynamic", level="High"):
        super().__init__(name, typing, level)


class Java(ProgrammingLanguage):
    def __init__(self, name="Java", typing="Static", level="High"):
        super().__init__(name, typing, level)


# jezyk1 = Python()
# print(jezyk1)
# jezyk2 = Java()
# print(jezyk2)
# jezyk3 = ProgrammingLanguage("C#", "Static", "High")
# print(jezyk3)
        

# Przykład 3
class Person:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Person):
    def __init__(self, imie, nazwisko, numer_indeksu):
        super().__init__(imie, nazwisko)
        self.numer_indeksu = numer_indeksu

    def studiuj(self):
        print(f"{self.imie} {self.nazwisko} studiuje.")


class Lecturer(Person):
    def __init__(self, imie, nazwisko, przedmiot):
        super().__init__(imie, nazwisko)
        self.przedmiot = przedmiot

    def wykladaj(self):
        print(f"{self.imie} {self.nazwisko} wyklada przedmiot: {self.przedmiot}")


class College:
    def __init__(self, imie_lecturer, nazwisko_lecturer, przedmiot, imie_student, nazwisko_student, numer_indeksu):
        # Inicjalizacja obiektów klas Student i Lecturer wewnątrz klasy College
        self.lecturer = Lecturer(imie_lecturer, nazwisko_lecturer, przedmiot)
        self.student = Student(imie_student, nazwisko_student, numer_indeksu)

    def wyklad(self):
        # Wywołanie metody wykladaj z klasy Lecturer oraz metody studiuj z klasy Student
        self.lecturer.wykladaj()
        self.student.studiuj()


# Przykład użycia:
# college = College("Jan", "Kowalski", "Matematyka", "Anna", "Nowak", 123456)
# college.wyklad()


class Rodzic:
    # Inicjalizacja atrybutów instancji dla rodzica
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Jestem rodzicem. Nazywam się {self.imie} i mam {self.wiek} lat.")


class Dziecko:
    # Inicjalizacja atrybutów instancji dla dziecka
    def __init__(self, imie, wiek, hobby):
        self.imie = imie
        self.wiek = wiek
        self.hobby = hobby

    def przedstaw_sie(self):
        print(f"Jestem dzieckiem. Nazywam się {self.imie}, mam {self.wiek} lat i moje hobby to {self.hobby}.")


class Dziedzic(Rodzic, Dziecko):
    # Inicjalizacja atrybutów instancji dla dziedzica
    # Wywołanie konstruktorów klas nadrzędnych
    def __init__(self, imie_rodzica, wiek_rodzica, imie_dziecka, wiek_dziecka, hobby):
        Rodzic.__init__(self, imie_rodzica, wiek_rodzica)
        Dziecko.__init__(self, imie_dziecka, wiek_dziecka, hobby)
        # Dodanie atrybutów unikalnych dla dziedzica
        self.imie_rodzica = imie_rodzica
        self.wiek_rodzica = wiek_rodzica

    def przedstaw_sie(self):
        print(f"Jestem dziedzicem. Nazywam się {self.imie}, mam {self.wiek} lat i moje hobby to {self.hobby}. "
              f"Mój rodzic to {self.imie_rodzica} i ma {self.wiek_rodzica} lat.")


# Przykładowe użycie:
# dziedzic = Dziedzic("Anna", 35, "Tomek", 8, "gry komputerowe")
# dziedzic.przedstaw_sie()


class Bohater:
    def __init__(self, imie):
        self.imie = imie
        self.poziom = 1
        self.hp = 100
        self.mp = 50

    def przedstaw_sie(self):
        print(f"Jestem bohaterem o imieniu {self.imie}.")
        print(f"Poziom: {self.poziom}, HP: {self.hp}, MP: {self.mp}")


class Wojownik(Bohater):
    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "Wojownik"
        self.atak = 10
        self.obrona = 5


class Mag(Bohater):
    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "Mag"
        self.atak = 5
        self.obrona = 3
        self.mp = 100


class Łotrzyk(Bohater):
    def __init__(self, imie):
        super().__init__(imie)
        self.profesja = "Łotrzyk"
        self.atak = 8
        self.obrona = 2
        self.hp = 80


# # Przykład użycia:
# imie = input("Podaj imię bohatera: ")
# wybor = input("Wybierz rodzaj bohatera: (W - Wojownik, M - Mag, L - Łotrzyk): ").upper()
# if wybor == "W":
#     bohater = Wojownik(imie)
# elif wybor == "M":
#     bohater = Mag(imie)
# elif wybor == "L":
#     bohater = Łotrzyk(imie)
# else:
#     print("Niepoprawny wybór.")
# if wybor in ["W", "M", "L"]:
#     bohater.przedstaw_sie()


def pokaz_atrybuty_domyslne():
    # Tworzymy instancje każdej klasy, aby uzyskać dostęp do domyślnych atrybutów
    wojownik = Wojownik("")
    mag = Mag("")
    lotrzyk = Łotrzyk("")

    # Iterujemy po każdej klasie i wyświetlamy domyślne atrybuty
    for klasa in [wojownik, mag, lotrzyk]:
        print(f"Klasa: {type(klasa).__name__}")
        print(f" - Imię: {klasa.imie}")
        print(f" - Poziom: {klasa.poziom}")
        print(f" - HP: {klasa.hp}")
        print(f" - MP: {klasa.mp}")
        if isinstance(klasa, Wojownik):
            print(f" - Profesja: {klasa.profesja}")
            print(f" - Atak: {klasa.atak}")
            print(f" - Obrona: {klasa.obrona}")
        elif isinstance(klasa, Mag):
            print(f" - Profesja: {klasa.profesja}")
            print(f" - Atak: {klasa.atak}")
            print(f" - Obrona: {klasa.obrona}")
        elif isinstance(klasa, Łotrzyk):
            print(f" - Profesja: {klasa.profesja}")
            print(f" - Atak: {klasa.atak}")
            print(f" - Obrona: {klasa.obrona}")
        print("-" * 30)

# Przykład użycia funkcji
# pokaz_atrybuty_domyslne()


# Przykład 4
class Employee:
    def __init__(self):
        self.current_id = 1
        self.contacts = []

    def display_person(self):
        return self.contacts

    def add_empployee(self, name, phone, email):
        contact = {
            "id": self.current_id,
            "name": name,
            "email": email,
        }
        self.contacts.append(contact)
        self.current_id += 1

    def remove_employee(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                self.contacts.remove(contact)
                return True
        return False


employee_obj = Employee()
employee_obj.add_empployee("Jan Kowalski", "123456789", "jan.kowalski@com")
employee_obj.add_empployee("Anna Nowak", "987654321", "anna.nowak@com")
employee_obj.add_empployee("Adam Nowak", "987654321", "adam.nowak@com")
print(employee_obj.display_person())
employee_obj.remove_employee(1)
print(employee_obj.display_person())

# MRO
        
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# print(D.mro())


# Kontenery tworzone przy użyciu dziedziczenia

class Zwierze:
    def __init__(self):
        self.cecha_zwierzeca = "Zwierzęca cecha"
        self.cecha_wspolna = "Cecha wspólna zwierzęcia"

    def odglos(self):
        pass                                


class Ptak(Zwierze):
    def __init__(self):
        super().__init__()
        self.cecha_wspolna = "Cecha wspólna ptaka"
        self.cecha_ptaka = "Cecha ptaka"
    
    def odglos(self):
        # super().odglos()
        print("Ptak wydaje odgłos")

class Ssak(Zwierze):
    def __init__(self):
        super().__init__()
        self.cecha_wspolna = "Cecha wspólna ssaka"
        self.cecha_ssaka = "Cecha ssaka"
    
    def odglos(self):
        print("Ssak wydaje odgłos")


class Hybryda(Ptak, Ssak):
    def __init__(self):
        super().__init__()


# Przykład użycia:
# hybryda = Hybryda()
# print(hybryda.cecha_zwierzeca)
# print(hybryda.cecha_ptaka)
# print(hybryda.cecha_ssaka)
# print(hybryda.cecha_wspolna)
# print(Hybryda.__mro__)
# hybryda.odglos()


class Kontener:
    def __init__(self):
        self.elementy = []

    def dodaj_element(self, element):
        self.elementy.append(element)

    def usun_element(self, element):
        if element in self.elementy:
            self.elementy.remove(element)
        else:
            print(f"{element} nie znaleziono w kontenerze.")

    def wyswietl_elementy(self):
        print("Elementy w kontenerze:")
        for element in self.elementy:
            print(element)


class Stos(Kontener):
    def __init__(self):
        super().__init__()

    def dodaj_na_stos(self, element):
        self.dodaj_element(element)

    def usun_z_stosu(self):
        if self.elementy:
            return self.elementy.pop()
        else:
            print("Stos jest pusty.")

    def wyswietl_stos(self):
        print("Elementy na stosie:")
        for element in reversed(self.elementy):
            print(element)


# Przykład użycia:
# stos = Stos()
# stos.dodaj_na_stos(1)
# stos.dodaj_na_stos(2)
# stos.dodaj_na_stos(3)
# stos.wyswietl_stos()
# print("Usunięty element ze stosu:", stos.usun_z_stosu())
# stos.wyswietl_stos()


# Klasa Bohatera
class Bohater:
    def __init__(self, imie, sila):
        self.imie = imie
        self.sila = sila

    def przedstaw_sie(self):
        print(f"Jestem {self.imie} o sile {self.sila}.")

# Klasa Wojownika dziedziczaca po Bohaterze
class WojownikDwa(Bohater):
    def __init__(self, imie, sila):
        super().__init__("Wojownik-" + imie, sila * 2)
        # super().__init__(self.__class__.__name__ + "-" + imie, sila * 2)


# bohater = Bohater("Artur", 10)
# bohater.przedstaw_sie()

# wojownik = WojownikDwa("Jan", 15)
# wojownik.przedstaw_sie()


from collections import UserList, UserDict, UserString

# Tworzymy własną klasę kontenera dziedziczącą po UserList
class CustomList(UserList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def custom_method(self):
        return f"Niestandardowa metoda dla CustomList: {self.data}"

    def count_elements(self):
        return f"Liczba elementów w CustomList: {len(self.data)}"
    
    def append(self, item):
        return ValueError("Nie można dodawać elementów do klasy CustomList")

# Tworzymy własną klasę kontenera dziedziczącą po UserDict
class CustomDict(UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def custom_method(self):
        return f"Niestandardowa metoda dla CustomDict: {self.data}"

    def count_keys_values(self):
        return f"Liczba kluczy w CustomDict: {len(self.data)}, Liczba wartości w CustomDict: {len(self.data.values())}"

    def find_key(self, value):
        # Znajduje klucz na podstawie wartości
        for key, val in self.data.items():
            if val == value:
                return key
        return None

    def find_value(self, key):
        # Znajduje wartość na podstawie klucza
        return self.data.get(key, None)
    

# Tworzymy własną klasę kontenera dziedziczącą po UserString
class CustomString(UserString):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def custom_method(self):
        return f"Niestandardowa metoda dla CustomString: {self.data}"

    def count_characters(self):
        return f"Liczba znaków w CustomString: {len(self.data)}"

# Przykład użycia naszych niestandardowych kontenerów
custom_list = CustomList([1, 2, 3, 4, 5])

custom_dict = CustomDict({'a': 1, 'b': 2, 'c': 3})

key_for_value = custom_dict.find_key(2)
value_for_key = custom_dict.find_value('b')

custom_string = CustomString("Hello, World!")

# Wywołujemy niestandardowe metody dla każdego kontenera
# print(custom_list.custom_method())
# print(custom_list.count_elements())
# print(custom_list.append(6))
# print(custom_list.count_elements())

# print(custom_dict.custom_method())
# print(custom_dict.count_keys_values())
# print(custom_dict.find_key(2))
# print(custom_dict.find_value('a'))

# print(custom_string.custom_method())
# print(custom_string.count_characters())

