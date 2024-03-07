'''
2. Metoda __init__
'''

# Przykład 1 - tworzenie instancji klasy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Tworzenie instancji klasy Person
# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)

# Wywołanie metody introduce dla każdej instancji
# print(person1.introduce())  # Wyświetli "My name is Alice and I am 30 years old."
# print(person2.introduce())  # Wyświetli "My name is Bob and I am 25 years old."


# Przykład 2 - wartości domyślne
class Person:
    def __init__(
            self, 
            name="Anonymous", 
            age=0
            ):
        self.name = name
        self.age = age

# Użycie domyślnych wartości argumentów
# anonymous_person = Person()
# print(anonymous_person.name)  # Wyświetli "Anonymous"


# Przykład 3 - init a dziedzieczenie
class Parent:
    def __init__(self):
        print("Parent initialized")

class Child(Parent):
    def __init__(self):
        print("Child initialized")
        super().__init__()  # Wywołanie konstruktora klasy bazowej

# Utworzenie obiektu klasy Child
# child = Child()


# Przykład 4 - walidacja danych
class User:
    def __init__(self, username, email):
        self.username = self.validate_username(username)
        self.email = self.validate_email(email)

    def validate_username(self, username):
        if len(username) < 5:
            raise ValueError("Username must be at least 5 characters long.")
        return username

    def validate_email(self, email):
        # Tutaj można dodać bardziej zaawansowane sprawdzanie poprawności adresu email
        if "@" not in email:
            raise ValueError("Invalid email address.")
        return email

# Utworzenie obiektu klasy User z walidacją danych
# user = User("john123", "john")
# print(user)
