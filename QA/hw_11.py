'''
Zadanie dpomowe 11 - opis

Dodawać pole Birthday. To pole jest opcjonalne, ale może być tylko jedno.
Dodamy też funkcjonalność do pracy z Birthday w klasie Record, a mianowicie funkcję days_to_birthday, która zwraca liczbę dni do następnych urodzin.
Dodamy funkcjonalności sprawdzania poprawności wartości dla pól Phone, Birthday.
Dodamy paginacji (wyjście strona po stronie) dla AddressBook dla sytuacji, gdy książka jest bardzo duża i trzeba pokazać zawartość w częściach, a nie wszystkie naraz. Implementujemy to poprzez utworzenie iteratora nad rekordami.

Kryteria akceptacji:
Klasa AddressBook implementuje metodę iterator, która zwraca generator przez rekordy AddressBook i zwraca widok dla N rekordów w jednej iteracji.
Klasa Record przyjmuje jeszcze jeden dodatkowy (opcjonalny) argument klasy Birthday
Klasa Record implementuje metodę days_to_birthday, która zwraca liczbę dni do następnych urodzin kontaktu, jeśli podano datę urodzin.
Logika setter i getter dla atrybutów value dziedziczących po Field.
Sprawdzenie poprawności podrzędnego setter numeru telefonu dla value klasy Phone.
Sprawdzenie poprawności podrzędnego settera daty urodzin dla wartości klasy Birthday.
'''

from datetime import datetime


class Field:
    def __init__(self, value=None):
        self.value = value

    def validate(self):
        # Implementacja walidacji, w zależności od konkretnego pola
        pass

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        self.validate()


class Phone(Field):
    def validate(self):
        if not self.value.isdigit(): # Kryterium akceptacji: Sprawdzenie poprawności podrzędnego setter numeru telefonu dla value klasy Phone.
            raise ValueError("Numer telefonu musi zawierać tylko cyfry.")
        if len(self.value) < 9 or len(self.value) > 15:
            raise ValueError("Numer telefonu musi zawierać pomiędzy 9 a 15 cyfr.")


class Birthday(Field):
    def validate(self):
        try:
            datetime.strptime(self.value, '%Y-%m-%d')  # Kryterium akceptacji: Sprawdzenie poprawności podrzędnego settera daty urodzin dla wartości klasy Birthday.
        except ValueError:
            raise ValueError("Niepoprawny format daty (YYYY-MM-DD).")


class Record:
    def __init__(self, name, phone=None, birthday=None):  # Kryterium akceptacji: Klasa Record przyjmuje jeszcze jeden dodatkowy (opcjonalny) argument klasy Birthday
        self.name = Field(name)
        self.phone = Phone(phone)
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.get_value():
            today = datetime.today()
            birthday_date = datetime.strptime(self.birthday.get_value(), '%Y-%m-%d')  # Kryterium akceptacji: Klasa Record implementuje metodę days_to_birthday, która zwraca liczbę dni do następnych urodzin kontaktu, jeśli podano datę urodzin.
            next_birthday = datetime(today.year, birthday_date.month, birthday_date.day)
            if today > next_birthday:
                next_birthday = datetime(today.year + 1, birthday_date.month, birthday_date.day)
            delta = next_birthday - today
            return delta.days
        else:
            return None


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def __iter__(self):
        return iter(self.records)

    def get_records_page(self, page_num, page_size):
        start_index = (page_num - 1) * page_size
        end_index = min(start_index + page_size, len(self.records))
        return self.records[start_index:end_index]


# Przykładowe użycie:
if __name__ == "__main__":
    # Tworzymy książkę adresową
    address_book = AddressBook()

    # Dodajemy rekordy
    record1 = Record("John Doe", "123456789", "1980-05-20")
    record2 = Record("Jane Smith", "987654321", "1990-10-15")
    address_book.add_record(record1)
    address_book.add_record(record2)

    # Sprawdzamy dni do następnych urodzin
    for record in address_book:
        days = record.days_to_birthday()
        if days is not None:
            print(f"Dni do urodzin {record.name.get_value()}: {days}")
        else:
            print(f"Nie dodano daty urodzin dla {record.name.get_value()}")

    # Przykład iteracji po książce adresowej z paginacją
    page_num = 1
    page_size = 2
    while True:
        records_page = address_book.get_records_page(page_num, page_size)
        if not records_page:
            break
        print(f"Strona {page_num}:")
        for record in records_page:
            print(f"{record.name.get_value()}, {record.phone.get_value()}, {record.birthday.get_value()}")
        page_num += 1
