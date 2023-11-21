# ---------------------- REPL ---------------------- #
# REPL - Read, Evaluate, Print, Loop
# Uruchomienie REPL: python lub python3 w terminalu
# Wyjście z REPL: exit()

# ---------------------- LICZBY ---------------------- #
# x = 5 # deklaracja zmiennej x typu int i przypisanie jej wartości 5
# y  = 4 # deklaracja zmiennej y typu float i przypisanie jej wartości 4.5
# z = x / y
# print(int(z)) # 9.5

# Liczby zespolone/ complex
# complex_number = 5 + 2j
# print(complex_number)


# ---------------------- NONE ---------------------- #
# x = None
# print(x)
# print(type(x))

# def sample_none_function():
#     pass

# print(sample_none_function())

# ---------------------- BOOLEAN ---------------------- #
# x = True
# print(x)

# x = False
# y = False
# is_equal = x == y  # False, ponieważ x nie jest równe y
# print(is_equal)



# sample_list = [1, 2, 3, 4, 5, 9, 11]
# print(len(sample_list))  # 7
# is_list_bigger_than_3 = len(sample_list) > 3  # True, ponieważ lista ma więcej niż 3 elementy
# print(is_list_bigger_than_3)

# sample_var = "Python"
# is_python = sample_var == "Python"  # True, ponieważ zmienna zawiera "Python"
# print(is_python)

# conditionOne = False
# conditionTwo = True
# conditionThree = False
# are_conditions_met = conditionOne and conditionTwo or conditionThree  # False, ponieważ oba warunki muszą być spełnione
# print(are_conditions_met)

# conditionOne = 'hi'
# conditionTwo = 'hi'
# conditionThree = 'hi'
# are_conditions_met = conditionOne == conditionTwo == conditionThree  # True, ponieważ jeden z warunków jest spełniony
# print(are_conditions_met)

# ---------------------- OPERATORY ---------------------- #
'''
+ - dodawanie
- - odejmowanie
* - mnożenie
/ - dzielenie
// - dzielenie bez reszty
** - potęgowanie
% - modulo
'''
# import math, cmath

# x = 25
# y = 2
# z = 0

# print(x + y)  # 7

# print(x - y)  # 3

# print(x * y)  # 10

# print(x / y)  # 2.5

# print(x // y)  # 2

# print(x ** y)  # 25

# print(x % y)  # 1

# print(x / z)  # ZeroDivisionError: division by zero

# print(x ** 0.5)


# Pierwiastek kwadratowy
# sqrt_result = math.sqrt(x)

# Pierwiastek trzeciego stopnia
# cbrt_result = x**(1/3)
# print(cbrt_result)

# pierwiastek_minus_1 = x**(-1/2)
# pierwiastek_minus_1 = cmath.sqrt(-1)
# print(pierwiastek_minus_1)

# x = 'test '
# print(x*5)

# ---------------------- WPROWADZANIE DANYCH ---------------------- #

# name = input("Podaj swoje imię: ")
# print("Witaj " + name + "!")

# https://github.com/jameswylde/openai-chatgpt-terminal/blob/main/genie.py

# age = input("Podaj swój wiek: ")
# # Przypisuja zmienną age do zmiennej age, ale jako int
# int_age = int(age)
# print(f"Masz {int_age} lat!")

# ---------------------- FUNKCJE WBUDOWANE ---------------------- #

# with open("sample_text_file.txt", "a") as file:
#     file.write("Hello, World!\n")


# with open("sample_text_file.txt", "r") as file:
#     content = file.read()
#     print(content)

# my_list = [1, 2, 3, 4, 5]
# length = len(my_list)
# if_length_is_greater_than_3 = length > 3
# print(f"Length of the list: {length}")
# print(f"Is length greater than 3? {if_length_is_greater_than_3}")


# my_range = range(1, 60, 2)  # Generates numbers from 1 to 5
# for number in my_range:
#     print(number)


# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# print("Tuple as a list:", my_tuple)


# numbers = [10, 25, 5, 30.5, 15.0]
# maximum = max(numbers)
# print("Maximum number:", maximum)


# numbers = [10, 25, 5, 30, 15]
# minimum = min(numbers)
# print("Minimum number:", minimum)

# sample_absolute_number = abs(-5)
# print("Absolute number:", sample_absolute_number)  # Output: 5


# float_num = 3.78765
# rounded_num = round(float_num)
# print("Rounded number:", rounded_num)  # Output: 4


# my_list = [5, 2, 8, 1, 3]
# sorted_list = sorted(my_list)
# descending_list = sorted(my_list, reverse=True)
# print("Sorted list:", descending_list)  # Output: [1, 2, 3, 5, 8]


# sample_double_quotation_string = 'This is a " \"test\" string "test2"'
# triple_quotation_string = """This is \n a "test" string  "test2" """
# print(sample_double_quotation_string)

# import math
# from math import sqrt

# sqrt(25)
# print(sqrt(25))

from types_of_data import sample_function, test


if __name__ == '__main__':
    sample_function()
    test()
