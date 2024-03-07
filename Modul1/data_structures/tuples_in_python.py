# ------------------------ KROTKI ------------------------ #
'''
Operacje na Krotkach:
count(element): Zlicza ilość wystąpień elementu.
index(element): Zwraca indeks pierwszego wystąpienia elementu.
'''

def example_tuple_creation():
    '''
    Tworzenie Krotki
    '''
    my_tuple = (1, 2, 3)
    print(my_tuple)

# Operacje na Tupli
def example_tuple_index():
    '''
    Zwraca indeks pierwszego wystąpienia elementu.
    '''
    my_tuple = (1, 2, 3, 2)
    index = my_tuple.index(3)
    print(index)

def example_tuple_count():
    '''
    Zlicza ilość wystąpień elementu.
    '''
    my_tuple = (1, 2, 3, 2)
    count = my_tuple.count(3)
    print(count)

# Inne Metody
def example_tuple_len():
    '''
    Zwraca ilość elementów w krotce.
    '''
    my_tuple = (1, 2, 3)
    length = len(my_tuple)
    print(length)

def example_tuple_max():
    '''
    Zwraca największy element.
    '''
    my_tuple = (1, 2, 3)
    maximum = max(my_tuple)
    print(maximum)

def example_tuple_min():
    '''
    Zwraca najmniejszy element.
    '''
    my_tuple = (1, 2, 3)
    minimum = min(my_tuple)
    print(minimum)

def example_tuple_creation_with_strings():
    '''
    Tworzenie Krotki z ciągami znaków
    '''
    my_tuple = ("apple", "banana", "orange")
    print(my_tuple)

def example_tuple_index_with_strings():
    '''
    Zwraca indeks pierwszego wystąpienia elementu.
    '''
    my_tuple = ("apple", "banana", "orange", "banana")
    index = my_tuple.index("orange")
    print(index)

def example_tuple_count_with_strings():
    '''
    Zlicza ilość wystąpień elementu.
    '''
    my_tuple = ("apple", "banana", "orange", "banana")
    count = my_tuple.count("apple")
    print(count)

def example_tuple_len_with_strings():
    '''
    Zwraca ilość elementów w krotce.
    '''
    my_tuple = ("apple", "banana", "orange")
    length = len(my_tuple)
    print(length)


def example_tuple_max_with_strings():
    '''
    Zwraca największy element.
    Zwraca znak o najwyższej wartości ASCII w ciągu znaków.
    '''
    my_tuple = ("apple", "banana", "orange")
    maximum = max(my_tuple)
    print(maximum)

def example_tuple_min_with_strings():
    '''
    Zwraca najmniejszy element.
    Zwraca znak o najniższej wartości ASCII w ciągu znaków.
    '''
    my_tuple = ("apple", "banana", "orange")
    minimum = min(my_tuple)
    print(minimum)


# if __name__ == "__main__":
    # example_tuple_creation()
    # example_tuple_index()
    # example_tuple_count()
    # example_tuple_len()
#     example_tuple_max()
#     example_tuple_min()
    # example_tuple_creation_with_strings()
    # example_tuple_index_with_strings()
    # example_tuple_count_with_strings()
    # example_tuple_len_with_strings()
    # example_tuple_max_with_strings()
    # example_tuple_min_with_strings()

    # moj_ciag = "banana"
    # maksimum = max(moj_ciag)
    # minimum = min(moj_ciag)

    # print(f"Najwyższy znak: {maksimum} dla {moj_ciag}, wartość ASCII: {ord(maksimum)}")
    # print(f"Najniższy znak: {minimum} dla {moj_ciag}, wartość ASCII: {ord(minimum)}")