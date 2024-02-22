'''
Zadanie dpomowe 10 - opis

Klasę AddressBook, która dziedziczy po UserDict, a następnie dodamy do niej logikę wyszukiwania rekordów.
Klasa Record, która jest odpowiedzialna za logikę dodawania/usuwania/edycji opcjonalnych pól i przechowywanie wymaganego pola Name.
Klasa Field, która będzie rodzicem dla wszystkich pól, w której następnie zaimplementujemy logikę wspólną dla wszystkich pól.
Klasa Name, wymagane pole z nazwą.
Klasa Phone, opcjonalne pole z numerem telefonu, a jeden rekord (Record) może zawierać ich kilka.

Kryteria przyjęcia
Wszystkie klasy z zadania zostały zaimplementowane.
Rekordy Record w AddressBook są przechowywane jako wartości w słowniku. Wartość Record.name.value jest używana jako klucze.
Rekord Record przechowuje obiekt Name w osobnym atrybucie.
Rekord Record przechowuje listę obiektów Phone w osobnym atrybucie.
Record implementuje metody do dodawania/usuwania/edycji obiektów Phone.
AddressBook implementuje metodę add_record, która dodaje Record do self.data.
'''

import cmd
from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, number):
        self.number = number


class Record:
    def __init__(self, name):
        self.name = name # Kryterium akceptacji: Rekord Record przechowuje obiekt Name w osobnym atrybucie.
        self.phones = [] # Kryterium akceptacji: Rekord Record przechowuje listę obiektów Phone w osobnym atrybucie.

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print(f"Numer {phone} nie znaleziony.")

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
        else:
            print(f"Numer {old_phone} nie znaleziony.")


class AddressBook(UserDict):
    def add_record(self, record):
        """Dodaj rekord do książki."""
        self.data[record.name] = record # Kryterium akceptacji: AddressBook implementuje metodę add_record, która dodaje Record do self.data.  Rekordy Record w AddressBook są przechowywane jako wartości w słowniku. Wartość Record.name.value jest używana jako klucze.

    def remove_record(self, name):
        """Usuń rekord z książki."""
        if name in self.data:
            del self.data[name]
        else:
            print(f"Rekord dla {name} nie znaleziony.")

    def search_records(self, criteria):
        """Wyszukaj rekordu na podstawie określonego warunku."""
        results = []
        for name, record in self.data.items():
            if criteria.lower() in name.lower():
                results.append(record)
        return results


class AddressBookCLI(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.address_book = AddressBook()

    def do_add(self, line):
        """Dodaj nowy kontakt"""
        name = input("Podaj imię i nazwisko: ")
        record = Record(name)
        phone = input("Podaj numer telefonu (jeśli chcesz dodać): ")
        if phone:
            record.add_phone(phone)
        self.address_book.add_record(record)
        print("Kontakt dodany.")

    def do_search(self, line):
        """Wyszukaj kontakty"""
        criteria = input("Podaj kryteria wyszukiwania: ")
        results = self.address_book.search_records(criteria)
        if results:
            print("Znalezione kontakty:")
            for record in results:
                print(f"Imię i nazwisko: {record.name}")
                if record.phones:
                    for phone in record.phones:
                        print(f"Numer telefonu: {phone}")
                else:
                    print("Brak numeru telefonu.")
        else:
            print("Brak kontaktów pasujących do kryteriów wyszukiwania.")

    def do_edit_phone(self, line):
        """Edytuj numer telefonu w wybranym kontakcie"""
        name = input("Podaj imię i nazwisko kontaktu: ")
        if name in self.address_book.data:
            record = self.address_book.data[name]
            old_phone = input("Podaj istniejący numer telefonu: ")
            new_phone = input("Podaj nowy numer telefonu: ")
            record.edit_phone(old_phone, new_phone)
            print("Numer telefonu zaktualizowany.")
        else:
            print(f"Kontakt o nazwie {name} nie istnieje.")

    def do_remove_phone(self, line):
        """Usuń numer telefonu z wybranego kontaktu"""
        name = input("Podaj imię i nazwisko kontaktu: ")
        if name in self.address_book.data:
            record = self.address_book.data[name]
            phone = input("Podaj numer telefonu do usunięcia: ")
            record.remove_phone(phone)
            print("Numer telefonu usunięty.")
        else:
            print(f"Kontakt o nazwie {name} nie istnieje.")
            
    def do_remove(self, line):
        """Usuń kontakt"""
        name = input("Podaj imię i nazwisko kontaktu do usunięcia: ")
        self.address_book.remove_record(name)
        print("Kontakt usunięty.")

    def do_quit(self, line):
        """Zakończ program"""
        return True


if __name__ == "__main__":
    cli = AddressBookCLI()
    print("Witaj! Dostępne komendy:")
    print(" - add: Dodaj nowy kontakt")
    print(" - search: Wyszukaj kontakty")
    print(" - quit: Zakończ program")
    while True:
        command = input("> ").strip()
        if command == "add":
            cli.do_add("")
        elif command == "search":
            cli.do_search("")
        elif command == "quit":
            print("Do widzenia!")
            break
        else:
            print("Nieznana komenda. Dostępne komendy: add, search, quit")