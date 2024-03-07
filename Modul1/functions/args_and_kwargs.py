# ---------------------- Argumenty pozycyjne i nazwane ---------------------- #

# Argumenty pozycyjne są przekazywane do funkcji w kolejności, w jakiej zostały zdefiniowane.

def add_numbers(num1, num2):
    """
    Funkcja dodaje dwie liczby i wyświetla wynik.
    :param num1: Pierwsza liczba.
    :param num2: Druga liczba.
    """
    result = num1 / num2
    print(f"The division of {num1} and {num2} is: {result}")

# Wywołanie funkcji z dwoma parametrami
# add_numbers(3, 7)

# Argumenty nazwane są przekazywane do funkcji w dowolnej kolejności, ale muszą być przekazane z nazwą parametru.

# Wywołanie funkcji z dwoma parametrami
# add_numbers(num2=3, num1=7)


def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Wywołanie funkcji z argumentami nazwanymi
# display_info(age=25, name="Alice")
# display_info(25, "Adrian")


def say_hello(name="Jan"):
    if not name:
        print("Argument name nie został podany przez użytkownika. Został użyty domyślny argument.")
        return
    print(f"Hello, {name}!")
# say_hello()

# Argumenty z wartościami domyślnymi i bez wartości domyślnych
def print_max(num1=0, num2=0):
    if num1 > num2:
        print(num1, 'is maximum')
    else:
        print(num2, 'is maximum')

# Wywołanie funkcji z różną liczbą argumentów
# print_max()
# print_max(30)      # Domyślnie num2 przyjmuje wartość 0
# print_max(5, 2)


# Argumenty z wartościami domyślnymi i bez określonej kolejności
def sample_args_kwargs_func(num1, num2=5, num3=10):
    print('num1 is', num1, ', num2 is', num2, ', num3 is', num3)

# Wywołanie funkcji z argumentami nazwanymi
# sample_args_kwargs_func(3, 7)        # num1=3, num2=7, num3 przyjmuje wartość domyślną 10
# sample_args_kwargs_func(25, num3=24)    # num1=25, num2 przyjmuje wartość domyślną 5, num3=24
# sample_args_kwargs_func(num3=50, num1=100)  # num1=100, num2 przyjmuje wartość domyślną 5, num3=50

# *args, **kwargs

def print_args(arg1, arg2, arg3, *args, **kwargs):
    print(arg1)
    print(arg2)
    print(arg3)
    print(args)
    print(kwargs)

# Wywołanie funkcji z dowolną liczbą argumentów
# print_args(1, 'test', 5, 7, 'test2', 3, name='Jan', age=25)

def sum_all(*args):
    result = 0
    for num in args:
        result += num
    return result

# sum_all_args = sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 19, 20, 7.5)
# print(sum_all_args)

def save_to_file(path, *sample_args):
    with open(path, 'w') as file:
        for arg in sample_args:
            file.write(str(arg) + '\n')

save_to_file('test.txt', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'test')

num1 = 5
num2= 7

def change_num(num1):
    num1 = 10
    print(num1)

# change_num(num1)


def print_topics_and_levels(*topics, **levels):
    for topic in topics:
        print(f"Topic: {topic}")
    
    for key, value in levels.items():
        print(f"Level of {key}: {value}")

# Przykładowe użycie funkcji
# print_topics_and_levels("Python", "Django", "React", "AWS", "Azure", Python=3, Django=2, React=4)

def example_function(_):
    '''
    Symbol _ jest często używany jako zmienna tymczasowa, 
    zwłaszcza gdy wartość zmiennej nie jest istotna lub nie będzie używana. 
    Jest to również często stosowane jako zmienna zastępcza w przypadkach, 
    gdy zmienna o tej samej nazwie jest już używana, a chcemy uniknąć konfliktu nazw.
    '''
    print(f"Received argument: {_}")

# Przykładowe użycie funkcji
# example_function("Hello, this is an example.")


def analyze_string(_):
    """
    Analizuje ciąg znaków, wypisując jego długość i unikalne litery.
    
    :param _: Ciąg znaków do analizy.
    """
    length = len(_)

    print(f"Length of the string: {length}")

# Przykładowe użycie funkcji
# input_string = "programming"
# analyze_string(input_string)

def some_function_returning_tuple():
    # ... implementacja ...
    return 42, "Hello"

_, result = some_function_returning_tuple()
# print(result)


some_list = ["apple", "banana", "cherry"]

# for _, value in enumerate(some_list):
    # print(value)


def some_function(arg1, _, arg3):
    print(f"arg1: {arg1}")
    print(f"arg3: {arg3}")

# some_function("value1", "ignored", "value3")

def calculate_result():
    return 42

result = calculate_result()

# _, updated_result = result, result + 10
# print(updated_result)


# updated_result, _ = result, result + 10
# print(updated_result)

def zmienna_tymczasowa():
    return 42, "Hello"

# _, result = zmienna_tymczasowa()
# print(result)