'''
Zadanie dpomowe 12 - opis

Dodanie funkcji zapisywania książki adresowej na dysku i przywracania jej z dysku. Aby to zrobić, możesz wybrać dowolny protokół serializacji/deserializacji danych i zaimplementować metody, które pozwolą Ci zapisać wszystkie dane do pliku i załadować je z pliku.
Dodanie możliwości przeszukiwania przez użytkownika zawartości książki kontaktów, tak aby mógł znaleźć wszystkie informacje o jednym lub kilku użytkownikach za pomocą kilku cyfr numeru telefonu lub liter imienia itp.

Kryteria akceptacji:
Program nie traci danych po wyjściu z aplikacji i przywraca je z pliku.
Program wyświetla listę użytkowników, których nazwisko lub numer telefonu pasuje do wprowadzonego ciągu znaków.
'''

import pickle


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        # Sprawdź, czy rekord już istnieje
        for existing_record in self.records:
            if existing_record.name == record.name and existing_record.phone == record.phone:
                print(f"Rekord dla {record.name} o numerze telefonu {record.phone} już istnieje.")
                return  # Nie dodawaj zduplikowanego rekordu
        # Jeśli rekord nie istnieje, dodaj go
        self.records.append(record)

    def save_to_disk(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.records, file)

    def load_from_disk(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.records = pickle.load(file)
        except FileNotFoundError:
            print("Plik nie znaleziony. Tworzenie nowej książki adresowej.")

    def search_records(self, query):
        results = []
        for record in self.records:
            if query.lower() in record.name.lower() or query in record.phone:
                results.append(record)
        return results


if __name__ == "__main__":
    # Kryteria: Program nie powinien tracić danych po wyjściu i powinien je przywracać z pliku.
    address_book = AddressBook()

    # Wczytaj lub utwórz nową książkę adresową
    address_book.load_from_disk("address_book.dat")

    # Przykładowe rekordy
    record1 = Record("John Doe", "123456789")
    record2 = Record("Jane Smith", "987654321")

    # Dodaj rekordy
    address_book.add_record(record1)
    address_book.add_record(record2)

    # Zapisz na dysk
    address_book.save_to_disk("address_book.dat")

    # Kryteria: Program powinien wyświetlać listę użytkowników, których nazwisko lub numer telefonu pasuje do wprowadzonego ciągu znaków.
    # Wyszukaj rekordy
    query = input("Wprowadź nazwisko lub numer telefonu do wyszukania: ")
    results = address_book.search_records(query)
    if results:
        print("Wyniki wyszukiwania:")
        for result in results:
            print(f"Imię: {result.name}, Telefon: {result.phone}")
    else:
        print("Nie znaleziono pasujących rekordów.")
