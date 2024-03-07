class Record:
    def __init__(self, name, phone, city):
        self._name = name
        self._phone = phone
        self._city = city
        self.validate_record()  # Dodajemy wywołanie metody walidacji

    def __str__(self):
        return f"Name: {self._name}, Phone: {self._phone}, City: {self._city}"

    def _validate_phone(self, phone):
        # Sprawdzenie czy numer telefonu zawiera tylko cyfry
        return all(char.isdigit() for char in phone)

    def _validate_city(self, city):
        # Sprawdzenie czy miasto zawiera tylko litery
        return city.isalpha()

    def validate_record(self):
        if not self._validate_phone(self._phone):
            raise ValueError("Invalid phone number")
        if not self._validate_city(self._city):
            raise ValueError("Invalid city name")


class AddressBook:
    MAX_RECORDS = 5

    def __init__(self):
        self._records = []
        self._age = None  # Private attribute

    def add_record(self, record):
        if len(self._records) >= self.MAX_RECORDS:
            print("Address book is full")
            return
        self._records.append(record)

    def __str__(self):
        return '\n'.join(str(record) for record in self._records)


class AddressBookWithAge(AddressBook):
    def __init__(self):
        super().__init__()

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age


# Przykład użycia:
if __name__ == "__main__":
    # Tworzenie rekordów
    record1 = Record("John Doe", "123456789", "NewYork")
    record2 = Record("Jane Smith", "987654321", "LosAngeles")
    record3 = Record("Alice Johnson", "555123456", "Chicago")
    record4 = Record("Bob Brown", "123456789", "SanFrancisco")
    record5 = Record("Kate Williams", "987654321", "Seattle")
    record6 = Record("Mark Miller", "555123456", "Boston")

    # Tworzenie książki adresowej
    address_book = AddressBookWithAge()

    # Dodawanie rekordów do książki
    address_book.add_record(record1)
    address_book.add_record(record2)
    address_book.add_record(record3)
    address_book.add_record(record4)
    address_book.add_record(record5)
    address_book.add_record(record6)  # Wyświetla: Address book is full

    # Wyświetlanie książki adresowej
    print("Address Book:")
    print(address_book)

    # Ustawianie i pobieranie wieku
    address_book.set_age(30)
    print("Age:", address_book.get_age())  # Wyświetla: Age: 30
