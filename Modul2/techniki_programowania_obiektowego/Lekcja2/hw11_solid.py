from abc import ABC, abstractmethod
from datetime import datetime

# Abstrakcyjna klasa walidatora
class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        pass

# Konkretna implementacja walidatora dla numeru telefonu
class PhoneValidator(Validator):
    def validate(self, value):
        if not value.isdigit():
            raise ValueError("Numer telefonu musi zawierać tylko cyfry.")
        if len(value) < 9 or len(value) > 15:
            raise ValueError("Numer telefonu musi zawierać pomiędzy 9 a 15 cyfr.")

# Konkretna implementacja walidatora dla daty
class DateValidator(Validator):
    def validate(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Niepoprawny format daty (YYYY-MM-DD).")

# Klasa reprezentująca pole w rekordzie
class Field:
    def __init__(self, value=None, validator=None):
        self.value = value
        self.validator = validator

    # Metoda ustawiająca wartość pola, wywołująca walidację
    def set_value(self, value):
        if self.validator:
            self.validator.validate(value)
        self.value = value

    def get_value(self):
        return self.value

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        # Pola phone i birthday korzystają z klasy Field z walidatorami
        self.phone = Field(phone, PhoneValidator())
        self.birthday = Field(birthday, DateValidator())

    def days_to_birthday(self):
        if self.birthday.get_value():
            today = datetime.today()
            birthday_date = datetime.strptime(self.birthday.get_value(), '%Y-%m-%d')
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

if __name__ == "__main__":
    address_book = AddressBook()
    record1 = Record("John Doe", "123456789", "1990-05-15")
    record2 = Record("Jane Smith", "987654321", "1988-11-30")
    record3 = Record("Alice Wonderland", "555888777", "1995-03-20")

    address_book.add_record(record1)
    address_book.add_record(record2)
    address_book.add_record(record3)

    for record in address_book:
        days_to_birthday = record.days_to_birthday()
        if days_to_birthday is not None:
            print(f"Osoba: {record.name}, dni do urodzin: {days_to_birthday}")
        else:
            print(f"Osoba: {record.name}, nie podano daty urodzenia.")
