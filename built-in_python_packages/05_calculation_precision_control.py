'''
6. Kontrola precyzji obliczeń (decimal)

W Pythonie istnieje moduł decimal, który pozwala na kontrolę precyzji obliczeń.
Ze względu na sposób reprezentacji liczb w komputerze, niektóre obliczenia mogą być obarczone błędem.
Przykładowo, jeśli dodamy do siebie liczby 0.1 i 0.2, to wynik nie będzie równy 0.3, a 0.30000000000000004.
Aby uniknąć takich błędów, możemy użyć modułu decimal.
'''

from decimal import Decimal, getcontext

def decimal_example():
    """
    Przykład użycia modułu decimal.
    """
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
    # getcontext().prec = 3
    print(getcontext())
    decimal_number = Decimal(0.1) / Decimal(0.7)
    return decimal_number

# print(decimal_precision_control())


def average_of_decimal_numbers():
    """
    Przykład użycia modułu decimal do kontroli precyzji obliczeń.
    Getcontext() pozwala na kontrolę precyzji obliczeń (liczba miejsc po przecinku).
    """
    getcontext().prec = 3
    decimal_numbers = [Decimal(8), Decimal(10), Decimal(92), Decimal(5.4), Decimal(0.57)]
    average = sum(decimal_numbers) / len(decimal_numbers)
    return average

# print(average_of_decimal_numbers())