'''
5 . Metoda __getitem__
'''

# Przykład 1 - metoda __getitem__ w klasie MyList
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

# Utworzenie obiektu klasy MyList
# my_list = MyList([1, 2, 3, 4, 5])

# Dostęp do elementów za pomocą metody __getitem__()
# print(my_list[0])  # Wyświetli: 1
# print(my_list[3])  # Wyświetli: 4


# Przykład 2 - metoda __getitem__ w klasie AddressBook
class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, email):
        self.contacts[name] = email

    def __getitem__(self, name):
        return self.contacts.get(name, "Contact not found")

# Utworzenie obiektu klasy AddressBook
# address_book = AddressBook()

# Dodanie kilku kontaktów
# address_book.add_contact("John", "john@example.com")
# address_book.add_contact("Alice", "alice@example.com")
# address_book.add_contact("Bob", "bob@example.com")

# Wyświetlenie adresu e-mail za pomocą metody __getitem__()
# print(address_book["John"])  # Wyświetli: john@example.com
# print(address_book["Mary"])  # Wyświetli: Contact not found


'''
6 . Metoda __setitem__
'''

# Przykład 1 - metoda __setitem__ w klasie MyList
class MyList:
    def __init__(self):
        self.elements = []

    def __setitem__(self, index, value):
        self.elements[index] = value

    def append(self, value):
        self.elements.append(value)

# Utworzenie obiektu klasy MyList
my_list = MyList()

# Przypisanie wartości do elementów za pomocą metody __setitem__()
# my_list.append(1)
# my_list.append(2)
# my_list[1] = 3

# print(my_list.elements)  # Wyświetli: [1, 3]


# Przykład 2 - metoda __setitem__ w klasie LimitedDict
class LimitedDict:
    def __init__(self, limit):
        self.limit = limit
        self.data = {}

    def __setitem__(self, key, value):
        if len(self.data) >= self.limit:
            raise ValueError("Limit exceeded: cannot add more items")
        else:
            self.data[key] = value

# Utworzenie obiektu klasy LimitedDict z limitem 3 elementów
limited_dict = LimitedDict(3)

# Przypisanie wartości do kluczy za pomocą metody __setitem__()
limited_dict['a'] = 1
limited_dict['b'] = 2
limited_dict['c'] = 3

print(limited_dict.data)  # Wyświetli: {'a': 1, 'b': 2, 'c': 3}

# Próba przypisania więcej elementów niż wynosi limit
def add_more_items():
    try:
        limited_dict['d'] = 4
    except ValueError as e:
        print(e)  # Wyświetli: Limit exceeded: cannot add more items

add_more_items()