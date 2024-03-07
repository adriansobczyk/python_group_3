'''
6. Kontrola precyzji obliczeń (decimal)

W Pythonie istnieje moduł decimal, który pozwala na kontrolę precyzji obliczeń.
Ze względu na sposób reprezentacji liczb w komputerze, niektóre obliczenia mogą być obarczone błędem.
Przykładowo, jeśli dodamy do siebie liczby 0.1 i 0.2, to wynik nie będzie równy 0.3, a 0.30000000000000004.
Aby uniknąć takich błędów, możemy użyć modułu decimal.
Więcej informacji na temat modułu decimal można znaleźć pod adresem:
https://docs.python.org/3/library/decimal.html
'''

from decimal import Decimal, getcontext

def decimal_example():
    """
    Przykład użycia modułu decimal.
    """
    # decimal_number = float(0.1) + float(0.2)
    getcontext().prec = 3
    decimal_number = Decimal(0.1) + Decimal(0.2)
    return decimal_number

# print(decimal_example())


def string_representation_in_decimals():
    """
    Przykład użycia modułu decimal.
    """
    if Decimal('0.2') + Decimal('0.1') == Decimal('0.3'):
        return True
    else:
        return False

# print(string_representation_in_decimals())


def decimal_precision_control():
    """
    Przykład użycia modułu decimal do kontroli precyzji obliczeń.
    Getcontext() pozwala na kontrolę precyzji obliczeń (liczba miejsc po przecinku).
    """
    getcontext().prec = 1
    print(getcontext())
    decimal_number = Decimal(0.1) / Decimal(10)
    decimal_number = round(decimal_number, 2)
    return decimal_number

# print(decimal_precision_control())


def average_of_decimal_numbers():
    """
    Przykład użycia modułu decimal do kontroli precyzji obliczeń.
    Getcontext() pozwala na kontrolę precyzji obliczeń (liczba miejsc po przecinku).
    """
    getcontext().prec = 3
    D = Decimal
    decimal_numbers = [D(8), D(10), D(92), D(5.4), D(0.57)]
    average = sum(decimal_numbers) / len(decimal_numbers)
    return average

print(average_of_decimal_numbers())
