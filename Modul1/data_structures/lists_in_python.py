# ------------------------ LISTY ------------------------ #
'''
Dodawanie Elementów:

append(element): Dodaje element na koniec listy.
extend(iterable): Rozszerza listę o elementy z innego iterable.
insert(index, element): Wstawia element na określony indeks.
Usuwanie Elementów:

remove(element): Usuwa pierwsze wystąpienie danego elementu.
pop(index): Usuwa i zwraca element na danym indeksie.
clear(): Usuwa wszystkie elementy z listy.
Operacje na Elementach:

index(element): Zwraca indeks pierwszego wystąpienia elementu.
count(element): Zlicza ilość wystąpień elementu.
sort(): Sortuje elementy listy.
reverse(): Odwraca kolejność elementów.
Inne Metody:

copy(): Tworzy kopię listy.
len(): Zwraca ilość elementów w liście.
max(): Zwraca największy element.
min(): Zwraca najmniejszy element.
'''

def example_slice():
    '''
    Przykład użycia slice. Zwraca co drugi element listy. 
    Step = 2 czyli trzeci argument oznacza, że co drugi element listy zostanie zwrócony.
    '''
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice_obj = my_list[3:6:2]
    # sample_slice = slice(0, 6, 2)
    print(slice_obj)

def example_append():
    '''
    Dodaje element na koniec listy.
    '''
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)


def example_extend():
    '''
    Rozszerza listę o elementy z innego iterable.
    '''
    my_list = [1, 2, 3]
    another_list = [4, 5, 6]
    my_list.extend(another_list)
    print(my_list)


def dodaj_elementy():
    """
    Funkcja dodająca elementy do listy przy użyciu operatora +=
    
    Parametry:
    - do_listy: lista, do której dodawane będą elementy
    - *elementy: elementy do dodania do listy
    """
    my_list = [1, 2, 3]
    elementy_dodane = [4, 5, 6]
    my_list += elementy_dodane
    print(my_list)


def example_insert():
    '''
    Wstawia element na określony indeks.
    '''
    my_list = [1, 2, 3]
    my_list.insert(1, 4)
    print(my_list)

def example_remove():
    '''
    Usuwa pierwsze wystąpienie danego elementu.
    '''
    my_list = [1, 2, 5, 2]
    print(f"Przed usunięciem: {my_list}")
    my_list.remove(2)
    print(f"Po usunięciu: {my_list}")

def example_pop():
    '''
    Usuwa i zwraca element na danym indeksie.
    '''
    my_list = [1, 2, 3]
    print("Przed usunięciem:", my_list)
    popped_element = my_list.pop(2)
    print("Po usunięciu:", my_list)
    print("Usunięty element:", popped_element)
    print(my_list)

def example_clear():
    '''
    Usuwa wszystkie elementy z listy.
    '''
    my_list = [1, 2, 3]
    my_list.clear()
    print(my_list)

def example_index():
    '''
    Zwraca indeks pierwszego wystąpienia elementu.
    '''
    my_list = [1, 2, 3, 2]
    index = my_list.index(3)
    print(index)

def example_count():
    '''
    Zlicza ilość wystąpień elementu.
    '''
    my_list = [1, 2, 3, 2]
    count = my_list.count(3)
    print(count)

def example_sort():
    '''
    Sortuje elementy listy.
    '''
    my_list = [3, 1, 4, 1, 5, 9, 2]
    my_list.sort()
    print(my_list)

def example_reverse():
    '''
    Odwraca kolejność elementów.
    '''
    my_list = [1, 2, 3]
    my_list.reverse()
    print(my_list)

def example_copy():
    '''
    Tworzy kopię listy.
    '''
    my_list = [1, 2, 3]
    print(my_list)
    copy_of_list = my_list.copy()
    print(copy_of_list)

def example_len():
    '''
    Zwraca ilość elementów w liście.
    '''
    my_list = [1, 2, 3]
    length = len(my_list)
    print(length)

def example_max():
    '''
    Zwraca największy element.
    '''
    my_list = [1, 2, 3]
    maximum = max(my_list)
    print(maximum)

def example_min():
    '''
    Zwraca najmniejszy element.
    '''
    my_list = [1, 2, 3]
    minimum = min(my_list)
    print(minimum)

def append_method(string_list):
    '''
    Zwraca listę z dodanym elementem.
    '''
    string_list.append("pear")
    return string_list

def extend_method(string_list):
    '''
    Zwraca listę z dodanymi elementami.
    '''
    additional_fruits = ["pineapple", "watermelon"]
    string_list.extend(additional_fruits)
    return string_list

def insert_method(string_list):
    '''
    Zwraca listę z dodanym elementem na określonym indeksie.
    '''
    string_list.insert(2, "cherry")
    return string_list

def remove_method(string_list):
    '''
    Zwraca listę z usuniętym elementem.
    '''
    string_list.remove("orange")
    return string_list

def pop_method(string_list):
    '''
    Zwraca listę z usuniętym elementem na określonym indeksie.
    '''
    popped_fruit = string_list.pop(-1) # Usuwa ostatni element
    return string_list, popped_fruit

def index_method(string_list):
    '''
    Zwraca indeks pierwszego wystąpienia elementu.
    '''
    index_of_grape = string_list.index("grape")
    return index_of_grape

def count_method(string_list):
    '''
    Zwraca ilość wystąpień elementu.
    '''
    occurrences_of_kiwi = string_list.count("kiwi")
    return occurrences_of_kiwi

def reverse_method(string_list):
    '''
    Zwraca listę z odwróconą kolejnością elementów.
    '''
    string_list.reverse()
    return string_list

def sort_method(string_list):
    string_list.sort()
    return string_list


# def list_methods_with_strings():
    # string_list = ["apple", "banana", "orange", "grape", "kiwi"]
    # string_list = append_method(string_list)
    # string_list = extend_method(string_list)
    # string_list = insert_method(string_list)
    # string_list = remove_method(string_list)
    # string_list, popped_fruit = pop_method(string_list)
    # index_of_grape = index_method(string_list)
    # occurrences_of_kiwi = count_method(string_list, "kiwi")
    # string_list = reverse_method(string_list)
    # string_list = sort_method(string_list)

    # Wyświetl zmodyfikowaną listę i wyniki każdej metody
    # print("Modified List:", string_list)
    # print("Popped Fruit:", popped_fruit)
    # print("Index of 'grape':", index_of_grape)
    # print("Occurrences of 'kiwi':", occurrences_of_kiwi)
    # print("Reversed List:", string_list)
    # print("Sorted List:", string_list)


# if __name__ == "__main__":
    # example_slice()
    # example_append()
    # dodaj_elementy()
    # example_extend()
    # example_insert()
    # example_remove()
    # example_pop()
    # example_clear()
    # example_index()
    # example_count()
    # example_sort()
    # example_reverse()
    # example_copy()
    # example_len()
    # example_max()
    # example_min()
    # list_methods_with_strings()

    # sample_dict_with_list = {
    #     "fruits": ["apple", "banana", "orange", "grape", "kiwi"]
    # }

    # extracted_list = sample_dict_with_list["fruits"]
    # extract_banan = extracted_list[1]
    # print(extract_banan)

    # sample_list = [1, 2, 3, 4, 5, 2, 4, 2, 2]
    # convert_to_set = set(sample_list)
    # print(convert_to_set)