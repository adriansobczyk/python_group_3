# Przykład 1

def say_hello():
    """
    Funkcja wyświetlająca napis Hello, World!
    """
    print('Hello, World!')

# Wywołanie funkcji
# say_hello()

# Przykład 2

def add_numbers(num1, num2):
    """
    Funkcja dodaje dwie liczby i wyświetla wynik.
    :param a: Pierwsza liczba.
    :param b: Druga liczba.
    """
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

# Wywołanie funkcji z dwoma parametrami
# add_numbers(2, 3)

# Przykład 3

def add_list_elements(my_list):
    """
    Funkcja dodaje wszystkie elementy listy i zwraca wynik.
    :param my_list: Lista do zsumowania.
    :return: Suma elementów listy.
    """
    total = sum(my_list)
    return total

# Przykład użycia funkcji z listą jako parametrem
# my_numbers = [1, 2, 3, 4, 5]
# result = add_list_elements(my_numbers)
# print(f"The sum of the list elements is: {result}")

# Przykład 4

def count_down(start_number):
    """
    Funkcja odlicza w dół od danej liczby do zera.
    :param start: Początkowa liczba do odliczania.
    """
    while start_number >= 0:
        print(start_number)
        start_number -= 1

# Przykład użycia funkcji z pętlą while
# count_down(8)


# Przykład 5

def find_element(my_list, target):
    """
    Funkcja sprawdza, czy dany element jest obecny w liście.
    :param my_list: Lista do sprawdzenia.
    :param target: Element do znalezienia.
    """
    for element in my_list:
        if element == target:
            print(f"Element {target} found!")
            break
    else:
        print(f"Element {target} not found in the list.")

# Przykład użycia funkcji z break
# my_numbers = [1, 2, 3, 4, 5]
# find_element(my_numbers, 4)

# Przykład 6

def print_even_numbers(limit):
    """
    Funkcja drukuje parzyste liczby w zakresie do danej liczby.
    :param limit: Górny limit zakresu.
    """
    num = 0
    while num <= limit:
        if num % 2 == 0:
            print(num)
        num += 1

# Przykład użycia funkcji z pętlą while
# print_even_numbers(8)


# Przykład 7

def check_conditions(x, y):
    """
    Funkcja sprawdza różne warunki za pomocą operatorów logicznych.
    :param x: Pierwsza wartość.
    :param y: Druga wartość.
    """
    if x > 0 and y > 0:
        print("Obie liczby są dodatnie.")
        # return True

    if x < 0 or y < 0:
        print("Przynajmniej jedna liczba jest ujemna.")
        # return True

    if not (x == y):
        print("Liczby nie są sobie równe.")
        # return True
    # return print("Koniec sprawdzania.")

# Przykład użycia funkcji z operatorami logicznymi
# check_conditions(3, 4)
