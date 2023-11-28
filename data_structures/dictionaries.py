# ------------------------ SŁOWNIKI ------------------------ #
'''
Operacje na Słownikach:

keys(): Zwraca widok na klucze słownika.
values(): Zwraca widok na wartości słownika.
items(): Zwraca widok na pary klucz-wartość.
get(key, default): Zwraca wartość dla danego klucza, lub wartość domyślną.
Modyfikacja Słownika:

update(iterable): Aktualizuje słownik, dodając elementy z innego iterable.
pop(key, default): Usuwa i zwraca wartość dla danego klucza.
'''

def dictionary_keys_example():
    '''
    Przykładowy słownik z kluczami i wartościami typu int.
    '''
    int_dict = {1: 10, 
                2: 20, 
                3: 30, 
                4: 40, 
                5: 50
                }

    # Metoda słownika: keys() - zwraca widok na klucze słownika
    return int_dict.keys()

def dictionary_values_example():
    '''
    Przykładowy słownik z kluczami i wartościami typu str.
    '''
    str_dict = {
        "apple": "red", 
        "banana": "yellow", 
        "grape": "purple", 
        "kiwi": "brown"
        }

    # Metoda słownika: values() - zwraca widok na wartości słownika
    return str_dict.values()

def dictionary_items_example():
    '''
    Przykładowy słownik z kluczami i wartościami typu int i str.
    '''
    mixed_dict = {
        1: "one", 
        "two": 2, 
        3: "three", 
        "four": 4, 
        "five": "5"}

    # Metoda słownika: items() - zwraca widok na pary klucz-wartość
    return mixed_dict.items()

def dictionary_copy_example():
    '''
    Przykładowy słownik z kluczami i wartościami typu int.
    '''
    int_dict = {1: 10, 
                2: 20, 
                3: 30, 
                4: 40, 
                5: 50}

    # Metoda słownika: copy() - zwraca kopię słownika
    return int_dict.copy()

def demonstrate_copy_method(original_dict):
    '''
    Demonstruje działanie metody copy() na słowniku.
    '''
    original_dict = {1: 'one', 2: 'two', 3: 'three'}

    # Bez copy
    modified_dict = original_dict
    modified_dict[1] = 'modified'

    print(original_dict)

    # Z copy
    original_dict = {1: 'one', 2: 'two', 3: 'three'}
    copied_dict = original_dict.copy()
    copied_dict[1] = 'modified'

    print(copied_dict) 


def dictionary_clear_example():
    '''
    Przykładowy słownik z kluczami i wartościami typu str.
    '''
    str_dict = {"apple": "red", "banana": "yellow", "grape": "purple", "kiwi": "brown"}

    # Metoda słownika: clear() - usuwa wszystkie elementy ze słownika
    str_dict.clear()
    return str_dict

def dictionary_fromkeys_example():
    '''
    Przykładowy słownik z kluczami typu str.
    '''
    # Dictionary method: fromkeys()
    keys = ["name", "age", "city"]
    default_value = "unknown"
    new_dict = dict.fromkeys(keys, default_value)
    print("Fromkeys:", new_dict)


def dictionary_get_example():
    '''
    Przykładowy słownik z kluczami i wartościami typu str.
    '''
    # Example dictionary
    my_dict = {"apple": "red", "banana": "yellow", "grape": "purple", "kiwi": "brown"}

    # Dictionary method: get()
    value = my_dict.get("banana")
    print("Get:", value)

def dictionary_pop_example():
    # Example dictionary
    my_dict = {"apple": "red", "banana": "yellow", "grape": "purple", "kiwi": "brown"}

    # Dictionary method: pop()
    removed_value = my_dict.pop("banana")
    print("Pop:", removed_value)

def dictionary_popitem_example():
    # Example dictionary
    my_dict = {"apple": "red", "banana": "yellow", "grape": "purple", "kiwi": "brown"}

    # Dictionary method: popitem()
    popped_item = my_dict.popitem()
    print("Popitem:", popped_item)

def dictionary_setdefault_example():
    # Example dictionary
    my_dict = {"apple": "red", "banana": "yellow", "grape": "purple", "kiwi": "brown"}

    # Dictionary method: setdefault()
    default_value = my_dict.setdefault("orange", "unknown")
    print("Setdefault:", my_dict)

def dictionary_update_example():
    # Example dictionaries
    dict1 = {"name": "John", "age": 30}
    dict2 = {"city": "New York", "age": 31}

    # Dictionary method: update()
    dict1.update(dict2)
    print("Update:", dict1)

if __name__ == "__main__":
    # Trigger each function here and print the results
    # print("Keys:", dictionary_keys_example())
    # print("Values:", dictionary_values_example())
    # print("Items:", dictionary_items_example())
    # print("Copy:", dictionary_copy_example())
    # print("Clear:", dictionary_clear_example())
    # print("Fromkeys:", dictionary_fromkeys_example())
    # print("Get:", dictionary_get_example())
    print("Pop:", dictionary_pop_example())
    # print("Popitem:", dictionary_popitem_example())
    # print("Setdefault:", dictionary_setdefault_example())
    # print("Update:", dictionary_update_example())

    # sample_dict = {'a': 1, 'b': 2, 'c': 3}
    # demonstrate_copy_method(sample_dict)