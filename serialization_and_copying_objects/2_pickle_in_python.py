'''
2. Pickle w Pythonie

Funkcje modułu pickle:
- dump() - zapisuje obiekt do pliku
- load() - wczytuje obiekt z pliku

obj - obiekt do serializacji
protocol - parametr określający wersję protokołu do serializacji
fix_imports - parametr określający, czy mają być stosowane poprawki do importów
encoding - parametr określający kodowanie znaków
errors - parametr określający sposób obsługi błędów kodowania znaków
'''

import pickle

# Przykład 1
# Lista do zserializowania
def sample_pickle_func():
    data_list = [1, 2, 3, 4, 5]

    # Serializacja listy do ciągu bajtów
    serialized_list = pickle.dumps(data_list) # fix_imports=True, encoding="ASCII", errors="strict"

    # Wyświetlenie zserializowanej listy
    print("Serialized List:", serialized_list)

    # Deserializacja ciągu bajtów do listy
    deserialized_list = pickle.loads(serialized_list)

    # Wyświetlenie deserializowanej listy
    print("Deserialized List:", deserialized_list)


# sample_pickle_func()


# Przykład 2
# Obiekt do serializacji
# data_to_serialize = {"name": "John", "age": 30}
# Serializacja do ciągu bajtów
# serialized_data = pickle.dumps(data_to_serialize)
# Zapis zserializowanych danych do pliku
# with open("2_serialized_data.pickle", "wb") as file:
#     file.write(serialized_data)
# Odczyt zserializowanych danych z pliku
# with open("2_serialized_data.pickle", "rb") as file:
    # deserialized_data = pickle.load(file)
# Wyświetlenie odtworzonych danych
# print(deserialized_data)


# Przykład 3
# Obiekt do serializacji
data_to_serialize = {"name": "John", "age": 30}

# funkcja serializująca
def serialize_data_to_file(data, file_name):
    # Serializacja do ciągu bajtów
    serialized_data = pickle.dumps(data)

    # Zapis zserializowanych danych do pliku
    with open(file_name, "wb") as file:
        file.write(serialized_data)

# funkcja deserializująca
def deserialize_data_from_file(file_name):
    # Odczyt zserializowanych danych z pliku
    with open(file_name, "rb") as file:
        deserialized_data = pickle.load(file)

    # Wyświetlenie odtworzonych danych
    print(deserialized_data)


# Wywołanie funkcji serializującej
# serialize_data_to_file(data_to_serialize, "2_serialized_data.pickle")
# Wywołanie funkcji deserializującej
# deserialize_data_from_file("2_serialized_data.pickle")

# Przykład 4
# Definicja klasy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Obiekt do zserializowania
# person = Person("John", 30)
# Serializacja obiektu do ciągu bajtów
# serialized_person = pickle.dumps(person)
# Wyświetlenie zserializowanego obiektu
# print("Serialized Person:", serialized_person)
# Deserializacja obiektu z ciągu bajtów
# deserialized_person = pickle.loads(serialized_person)
# Wyświetlenie deserializowanego obiektu
# print("Deserialized Person:")
# print("Name:", deserialized_person.name)
# print("Age:", deserialized_person.age)


# Przykład 5
# Definicja klasy Car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year})"

# Tworzenie obiektu klasy Car
# my_car = Car("Toyota", "Corolla", 2020)
# Serializacja obiektu klasy Car
# with open("car.pickle", "wb") as file:
    # pickle.dump(my_car, file)
# Deserializacja obiektu klasy Car
# with open("car.pickle", "rb") as file:
    # deserialized_car = pickle.load(file)
# Wyświetlanie deserializowanego obiektu
# print("Deserialized Car:", deserialized_car)
