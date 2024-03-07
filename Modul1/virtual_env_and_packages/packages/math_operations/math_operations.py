'''
Przykładowy moduł zawierający funkcje matematyczne.
'''

def add_nums(a, b):
    '''
    Dodawanie dwóch liczb.
    '''
    return a + b

def subtract_nums(a, b):
    '''
    Odejmowanie dwóch liczb.
    '''
    return a - b

def multiply_nums(a, b):
    '''
    Mnożenie dwóch liczb.
    '''
    return a * b

def divide_nums(a, b):
    '''
    Dzielenie dwóch liczb.
    '''
    return a / b

def pow_nums(a, b):
    '''
    Potęgowanie dwóch liczb.
    '''
    return a ** b

def sqrt_nums(a):
    '''
    Pierwiastek kwadratowy z liczby.
    '''
    return a ** 0.5

def factorial(a):
    '''
    Silnia z liczby.
    '''
    if a == 0:
        return 1
    return a * factorial(a - 1)

def is_prime(a):
    '''
    Sprawdzenie czy liczba jest pierwsza.
    '''
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True
