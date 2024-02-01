'''
10. Setter i Getter
'''

# Przykład 1 - bez użycia dekoratorów
class Person:
    def __init__(self, name):
        self._name = name  # Prywatne pole

    # Getter - umożliwia odczyt nazwy
    def get_name(self):
        return self._name

    # Setter - umożliwia zmianę nazwy
    def set_name(self, name):
        self._name = name

# Użycie klasy Person
# person = Person("John")
# print(person.get_name())  # Odczyt nazwy: John
# Zmiana nazwy za pomocą settera
# person.set_name("Alice")
# print(person.get_name())  # Odczyt nazwy: Alice


# Przykład 2 - z użyciem dekoratorów
class Person:
    def __init__(self, name):
        self._name = name  # Prywatne pole

    # Getter - umożliwia odczyt nazwy
    @property
    def name(self):
        return self._name

    # Setter - umożliwia zmianę nazwy
    @name.setter
    def name(self, value):
        self._name = value

# Użycie klasy Person
# person = Person("John")
# print(person.name)  # Odczyt nazwy: John
# Zmiana nazwy za pomocą settera
# person.name = "Alice"
# print(person.name)  # Odczyt nazwy: Alice


# Przykład 3
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    # Getter - odczyt temperatury w stopniach Celsiusza
    @property
    def celsius(self):
        return self._celsius

    # Setter - ustawienie temperatury w stopniach Celsiusza
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value

    # Getter - odczyt temperatury w stopniach Fahrenheita
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

# Użycie klasy Temperature
# temp = Temperature(25)
# print("Temperatura w stopniach Celsiusza:", temp.celsius)
# print("Temperatura w stopniach Fahrenheita:", temp.fahrenheit)
# # Zmiana temperatury za pomocą settera
# temp.celsius = 30
# print("Nowa temperatura w stopniach Celsiusza:", temp.celsius)
# print("Nowa temperatura w stopniach Fahrenheita:", temp.fahrenheit)
