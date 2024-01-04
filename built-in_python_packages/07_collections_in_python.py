'''
## 6. Kolekcje w Pythonie
'''

from collections import namedtuple, Counter, defaultdict, deque


def multiple_tuples():
    """
    Przykład użycia krotek.
    """
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    tuple3 = tuple1 + tuple2
    return tuple3

# print(multiple_tuples())
# print(type(multiple_tuples()))


def create_namedtuple(name, fields):
    """
    Tworzy i zwraca obiekt typu namedtuple.

    :param name: Nazwa dla namedtuple.
    :param fields: Lista pól namedtuple.
    :return: Obiekt namedtuple.
    """
    return namedtuple(name, fields)

# print(create_namedtuple('Person', ['name', 'surname', 'age']))


def namedtuple_example():
    """
    Przykład użycia namedtuple.
    """
    Person = namedtuple('Person', ['name', 'surname', 'age'])
    City = namedtuple('City', ['name', 'country', 'population'])
    person = Person('Jan', 'Kowalski', 25)
    city = City('New York', 'USA', 8000000)
    return person, city

# print(namedtuple_example())


def count_elements(iterable):
    """
    Zlicza ilość wystąpień każdego elementu w iterowalnym obiekcie.

    :param iterable: Iterowalny obiekt.
    :return: Obiekt Counter zawierający zliczone elementy.
    """
    return Counter(iterable)

# print(count_elements([1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]))


def counter_example():
    """
    Przykład użycia obiektu Counter.
    """
    list_of_numbers = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
    counter = Counter(list_of_numbers)
    print(counter[1])
    # print(counter[2])
    # print(counter[3])
    return counter

# print(counter_example())


def counter_sorted_by_most_common(counter):
    """
    Zwraca posortowany obiekt Counter według najczęściej występujących elementów.

    :param counter: Obiekt Counter.
    :return: Posortowany obiekt Counter.
    """
    return counter.most_common()

# print(counter_sorted_by_most_common(Counter([1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1])))


def counter_sorted_by_least_common(counter):
    """
    Zwraca posortowany obiekt Counter według najrzadziej występujących elementów.

    :param counter: Obiekt Counter.
    :return: Posortowany obiekt Counter.
    """
    return counter.most_common()[::-1]

# print(counter_sorted_by_least_common(Counter([1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1])))


def counter_subtract(counter1, counter2):
    """
    Odejmuje od siebie dwa obiekty Counter.

    :param counter1: Obiekt Counter.
    :param counter2: Obiekt Counter.
    :return: Obiekt Counter.
    """
    print(counter1)
    print(counter2)
    return counter1 - counter2

# print(counter_subtract(Counter([1, 2, 3, 4, 5, 1, 2, 2, 2, 1]), Counter([1, 2, 3, 4, 5])))


def create_defaultdict(default_factory, iterable):
    """
    Tworzy i zwraca obiekt defaultdict.

    :param default_factory: Fabryka domyślnych wartości.
    :param iterable: Iterowalny obiekt do zainicjowania defaultdict.
    :return: Obiekt defaultdict.
    """
    return defaultdict(default_factory, iterable)

# print(create_defaultdict(int, {'a': 1, 'b': 2, 'c': 3}))


def create_deque(iterable, maxlen=None):
    """
    Tworzy i zwraca obiekt deque.

    :param iterable: Iterowalny obiekt do zainicjowania deque.
    :param maxlen: Maksymalna długość deque (opcjonalne).
    :return: Obiekt deque.
    """
    return deque(iterable, maxlen=maxlen)

# print(create_deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], maxlen=3))


def sample_deque():
    """
    Przykład użycia obiektu deque.
    """
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    deque_object = deque(sample_list, maxlen=3)
    return deque_object

# print(sample_deque())
# print(type(sample_deque()))

def deque_append(deque_object, element):
    """
    Dodaje element na koniec deque.

    :param deque_object: Obiekt deque.
    :param element: Element do dodania.
    :return: Obiekt deque.
    """
    # print(deque_object)
    deque_object.append(element)
    return deque_object


# print(deque_append(deque([1, 2, 3, 4, 5]), 8))


def deque_appendleft(deque_object, element):
    """
    Dodaje element na początek deque.

    :param deque_object: Obiekt deque.
    :param element: Element do dodania.
    :return: Obiekt deque.
    """
    deque_object.appendleft(element)
    return deque_object

# print(deque_appendleft(deque([1, 2, 3, 4, 5]), 10))


def deque_pop(deque_object):
    """
    Usuwa ostatni element z deque.

    :param deque_object: Obiekt deque.
    :return: Obiekt deque.
    """
    deque_object.pop()
    return deque_object

# print(deque_pop(deque([1, 2, 3, 4, 5])))


def deque_popleft(deque_object):
    """
    Usuwa pierwszy element z deque.

    :param deque_object: Obiekt deque.
    :return: Obiekt deque.
    """
    deque_object.popleft()
    return deque_object

# print(deque_popleft(deque([1, 2, 3, 4, 5])))

def deque_insert(deque_object, index, element):
    """
    Wstawia element do deque na podaną pozycję.

    :param deque_object: Obiekt deque.
    :param index: Indeks pozycji.
    :param element: Element do wstawienia.
    :return: Obiekt deque.
    """
    deque_object.insert(index, element)
    return deque_object

# print(deque_insert(deque([1, 2, 3, 4, 5]), 2, 10))