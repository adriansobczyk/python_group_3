def show_args_and_kwargs(*args, **kwargs):
    """
    Wyświetla zawartość *args i **kwargs.

    Parametry:
    - *args: argumenty pozycyjne
    - **kwargs: argumenty nazwane

    Zwraca:
    - None
    """
    print("Argumenty pozycyjne (*args):")
    for index, arg in enumerate(args):
        print(f"Argument {index + 1}: {arg}")

    print("\nArgumenty nazwane (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Przykład użycia:
# show_args_and_kwargs(1, 'abc', param1='X', param2=42)

def example_function(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

# Przykład użycia:
# example_function(1, 'abc', param1='X', param2=42)


# ---------------------- Krotki (Tuples) ---------------------- #
def explain_tuples():
    # Krotki są uporządkowanymi, niezmiennymi sekwencjami wartości.
    # Elementy krotki mogą być różnych typów danych.
    
    # Tworzenie krotki
    fruits_tuple = ('Orange', 'Banana', 'Apple', 'Pear', 'Cherry')
    # second_tuple = 1, 2, 3, 4, 5  # Nawiasy są opcjonalne

    print(type(fruits_tuple))

    # concatenated_tuple = fruits_tuple + second_tuple
    # print(concatenated_tuple)
    
    # Dostęp do elementów krotki za pomocą indeksów
    # first_fruit = fruits_tuple[0]
    # first_fruit = fruits_tuple[-2]
    # first_fruit = fruits_tuple[0:2] 
    # first_fruit = fruits_tuple[:2]
    # first_fruit = fruits_tuple[1:]
    # first_fruit = fruits_tuple[::2]
    # first_fruit = fruits_tuple[::-1]
    # del fruits_tuple[1]
    # print(first_fruit)
    # sorted_puple = sorted(fruits_tuple)
    # sorted_ = tuple(sorted(sorted_puple, key=len))
    # print(sorted_puple)
    # print(sorted_)
    
    # Krotki są niezmienne, nie można zmieniać ich elementów po utworzeniu
    # fruits_tuple[0] = 'Pear'  # To spowoduje błąd
    # fruits_tuple.pop(0)  # To spowoduje błąd
    # fruits_tuple.append('Pear')  # To spowoduje błąd
    # fruits_tuple = (2, 6, 'Orange')  # To jest dozwolone
    # print(fruits_tuple)
    
    # Wypisanie wszystkich elementów krotki
    # for fruit in fruits_tuple:
    #     print(fruit)
    
    # Sprawdzenie, czy element istnieje w krotce
    # if 'Banana' in fruits_tuple:
    #     print('Banana is in the tuple')


def sort_tuple_of_strings(my_tuple):
    """
    Sortuje krotkę zawierającą ciągi znaków (samego typu danych string).

    Parametry:
    - my_tuple: krotka, która ma zostać posortowana

    Zwraca:
    - Posortowaną krotkę
    """
    return tuple(sorted(my_tuple, key=len))

# Przykład użycia:

# Krotka z ciągami znaków
string_tuple = ('jabłko', 'banan', 'pomarańcza', 'gruszka', 'arbuz')

# Posortowana krotka
# sorted_string_tuple = sort_tuple_of_strings(string_tuple)


def count_characters_in_tuple(my_tuple):
    """
    Liczy długość znaków w każdym elemencie krotki.

    Parametry:
    - my_tuple: krotka elementów do analizy

    Zwraca:
    - Lista zawierająca długości znaków dla każdego elementu krotki
    """
    return [len(str(item)) for item in my_tuple]

# Krotka do analizy
my_tuple = (12, 'abc', 456, 'Python')

# Wynik
# lengths_of_tuple_elements = count_characters_in_tuple(my_tuple)


# ---------------------- Słowniki (Dictionaries) ---------------------- #
def explain_dicts():
    # Słowniki są kolekcjami par klucz-wartość.
    # Klucze muszą być unikalne, a wartości mogą być różnych typów danych.
    
    # Tworzenie słownika
    person = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    
    # Dostęp do wartości za pomocą klucza
    person_name = person['name']
    
    # Modyfikacja wartości w słowniku
    person['age'] = 31
    
    # Dodawanie nowej pary klucz-wartość
    person['occupation'] = 'Engineer'
    
    # Usuwanie elementu ze słownika
    del person['city']
    
    # Wypisanie wszystkich kluczy i wartości w słowniku
    for key, value in person.items():
        print(f'{key}: {value}')
    
    # Sprawdzenie, czy klucz istnieje w słowniku
    if 'age' in person:
        print('Age is in the dictionary')


def sort_dict_by_values(my_dict):
    """
    Sortuje słownik według jego wartości.

    Parametry:
    - my_dict: słownik, który ma zostać posortowany

    Zwraca:
    - Posortowany słownik (krotka zawierająca pary klucz-wartość)
    """
    sorted_items = sorted(my_dict.items(), key=get_value)
    return dict(sorted_items)

def get_value(item):
    return item[1] # Zwraca wartość el

# Przykład użycia:

# Słownik z wartościami do posortowania
my_dictionary = {'jabłko': 3, 
                 'banan': 2, 
                 'pomarańcza': 5, 
                 'gruszka': 1, 
                 'arbuz': 4}

# Posortowany słownik
sorted_dict = sort_dict_by_values(my_dictionary)


def count_keys_in_dict(my_dict):
    """
    Liczy liczbę kluczy w słowniku.

    Parametry:
    - my_dict: słownik do analizy

    Zwraca:
    - Liczba kluczy w słowniku
    """
    return len(my_dict.keys())

# Przykład użycia:

# Słownik do analizy
my_dictionary = {'jabłko': 9, 'banan': 2, 'pomarańcza': 5, 'gruszka': 1, 'arbuz': 4}

# Wynik
keys_count = count_keys_in_dict(my_dictionary)


# Wywołanie funkcji wyjaśniających krotki i słowniki
# explain_tuples()
# print(sorted_string_tuple)
# print(lengths_of_tuple_elements)
# print('\n' + '-'*50 + '\n')  # Oddzielenie sekcji
# explain_dicts()
# print(sorted_dict)
# print(keys_count)

