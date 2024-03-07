'''
9. Enkapsulacja
'''

# Przykład 1
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount} units"
        else:
            return "Invalid amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount} units"
        else:
            return "Invalid amount or insufficient balance"

    def get_balance(self):
        return self.__balance

# account = BankAccount(1000)
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.get_balance()) 
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'


# Przykład 2
class Person:
    def __init__(self, name, age):
        self._name = name  # Chroniony atrybut
        self._age = age    # Chroniony atrybut

    # Właściwość do odczytu nazwy
    @property # getter - odczyt atrybutu _name (chronionego) - bez settera nie można zmienić wartości
    def name(self):
        return self._name

    # Właściwość do odczytu wieku
    @property
    def age(self):
        return self._age

# Użycie klasy Person
# person = Person("John", 30)
# print(person.name)  # Odczyt nazwy: John
# print(person.age)   # Odczyt wieku: 30

# Próba zmiany nazwy i wieku - nie jest to już możliwe bez setterów
# person.name = "Mike"  # To spowoduje błąd
# person.age = 35       # To również spowoduje błąd
