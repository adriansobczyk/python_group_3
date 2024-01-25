'''
Hermetyzacja (enkapsulacja) - ukrywanie zmiennych i metod przed innymi klasami
'''

# Przykład 1
class TemperatureSensor:
    def __init__(self):
        self.__temperature = 0  # Zmienna prywatna, dostępna tylko wewnątrz klasy

    def set_temperature(self, temperature):
        if temperature < -273.15:  # Temperatura absolutna (zero bezwzględne)
            print("Temperatura nie może być niższa niż zero bezwzględne.")
        else:
            self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature


# Użycie klasy TemperatureSensor
sensor = TemperatureSensor()
# Ustawienie temperatury
sensor.set_temperature(25)
# Pobranie temperatury
print("Aktualna temperatura:", sensor.get_temperature())
# Próba ustawienia temperatury poniżej zera bezwzględnego
sensor.set_temperature(-300)
print(sensor.__temperature) # Wywoła błąd AttributeError: 'TemperatureSensor' object has no attribute '__temperature'



# Przykład 2
class BankAccount:
   def __init__(self, account_name):
       self.account_name = account_name
       self._operations = 0
       self.__account_balance = 0
 
   def wpłata(self, amount):
       self.__account_balance += amount
       self._operations += 1
       print(f"Wpłacono {amount} PLN")
       
   def wypłata(self, amount):
       if amount > self.__account_balance:
           raise ValueError(f"Nie masz tyle pieniędzy")
       
       self.__account_balance -= amount
       self._operations += 1
       print(f"You withdrew ${amount}")
 
   def stan_konta(self):
       print(f"Pozostało {self.__account_balance} PLN na koncie")
 
 
# my_account = BankAccount("Konto bankowe")
# my_account.stan_konta()
# my_account.wpłata(1000)
# my_account.stan_konta()
# my_account.wypłata(500)
# my_account.stan_konta()
# print("Liczba operacji:", my_account._operations)
# print(my_account.__account_balance)
