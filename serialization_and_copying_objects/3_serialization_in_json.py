'''
Serializacja i deserializacja przy użyciu modułu JSON
'''

import json

# Przykład 1
# Serializacja - zapisanie danych do pliku
data = {
    "name": "Jan",
    "age": 30,
    "city": "Warszawa"
}

# with open('3_data.json', 'w') as file:
#     json.dump(data, file) #indent=4 - opcjonalny parametr, który dodaje wcięcia w celu poprawienia czytelności
# Deserializacja - odczytanie danych z pliku
# with open('3_data.json', 'r') as file:
#     data = json.load(file)
#     print(data)


# Przykład 2
# Definicja funkcji do serializacji danych do formatu JSON i zapisu do pliku
def serialize_and_save(data, file_path):
    json_string = json.dumps(data)
    with open(file_path, 'w') as file:
        file.write(json_string)

# Definicja funkcji do wczytania danych z pliku i deserializacji z formatu JSON
def load_and_deserialize(file_path):
    with open(file_path, 'r') as file:
        json_string = file.read()
        data = json.loads(json_string)
    return data

# Dane do serializacji
my_data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
file_path = '3_2_data.json'

# Serializacja danych i zapis do pliku
# serialize_and_save(my_data, file_path)
# print("Dane zostały zapisane do pliku:", file_path)
# Wczytanie danych z pliku i deserializacja
# loaded_data = load_and_deserialize(file_path)
# print("Wczytane dane:", loaded_data)


# Przykład 3
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {'name': self.name, 'age': self.age}

    def from_dict(data):
        return Person(data['name'], data['age'])

# Serializacja danych do formatu JSON
person = Person('John', 30)
json_string = json.dumps(person.to_dict())

# Deserializacja danych z formatu JSON
# data = json.loads(json_string)
# deserialized_person = Person.from_dict(data)

# print(deserialized_person.name)
# print(deserialized_person.age)

# Przykład 4
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def to_json(self):
        return json.dumps(self.__dict__)

    def from_json(json_string):
        data = json.loads(json_string)
        return Car(**data)

# Serializacja danych do formatu JSON
car = Car('Toyota', 'Camry', 2020)
json_string = car.to_json()

# Deserializacja danych z formatu JSON
deserialized_car = Car.from_json(json_string)

# print(deserialized_car.make)
# print(deserialized_car.model)
# print(deserialized_car.year)

