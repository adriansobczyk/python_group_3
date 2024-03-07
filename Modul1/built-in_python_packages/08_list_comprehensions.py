'''
8. List comprehensions
[wyrażenie for element in sekwencja if warunek]
'''

def list_comprehension():
    """
    Przykład użycia list comprehensions.
    """
    list_of_numbers = [1, 2, 3, 4, 5, 6, 2, 3]
    list_of_numbers_squared = [number ** 2 for number in list_of_numbers]
    return list_of_numbers_squared

# print(list_comprehension())


def list_comprehension_with_condition():
    """
    Przykład użycia list comprehensions z warunkiem.
    """
    list_of_numbers = [1, 2, 3, 4, 5, 6, 2, 3]
    list_of_numbers_squared = [number ** 2 for number in list_of_numbers if number % 2 == 0]
    return list_of_numbers_squared

# print(list_comprehension_with_condition())


def set_with_list_comprehension():
    """
    Przykład użycia list comprehensions do tworzenia zbioru.
    """
    list_of_numbers = [1, 2, 3, 4, 5, 6, 2, 3]
    set_of_numbers = {number ** 2 for number in list_of_numbers}
    return set_of_numbers

# print(set_with_list_comprehension())


def dict_with_list_comprehension():
    """
    Przykład użycia list comprehensions do tworzenia słownika.
    """
    list_of_numbers = [1, 2, 3, 4, 5, 6, 2, 3]
    dict_of_numbers = {number: number ** 2 for number in list_of_numbers}
    return dict_of_numbers

# print(dict_with_list_comprehension())


def create_dictionary_with_list_comprehension(keys, values):
    # Użycie list comprehension do stworzenia słownika
    my_dict = {key: value for key, value in zip(keys, values)} # zip() tworzy listę krotek z dwóch list
    # my_dict = {keys[i]: values[i] for i in range(min(len(keys), len(values)))} # bez zip() - wersja alternatywna
    return my_dict

# keys_list = ['name', 'age', 'city']
# values_list = ['John', 25, 'New York']
# result_dict = print(create_dictionary_with_list_comprehension(keys_list, values_list))


def display_birthday_date():
    '''
    Przykład użycia słownika do przechowywania dat urodzin.
    '''
    slownik_daty = {
        "Anna": "1990-05-15",
        "Jan": "1985-08-20",
        "Maria": "1995-02-10",
        "Adam": "1992-11-30",
        "Ewa": "1988-04-25",
    }

    # Pozwól użytkownikowi wprowadzić imię
    wprowadzone_imie = input("Podaj imię: ")

    # Sprawdź, czy imię istnieje w słowniku
    if wprowadzone_imie in slownik_daty:
        # Pobierz i wyświetl datę dla wprowadzonego imienia
        wynik = slownik_daty[wprowadzone_imie]
        return wynik 
    else:
        print("Brak danych dla podanego imienia.")

# Wywołaj funkcję obsługi słownika
print(display_birthday_date())