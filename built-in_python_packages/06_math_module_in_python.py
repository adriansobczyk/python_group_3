'''
## 6. Właściwości pakietów math, cmath
'''

import math
import cmath

def math_module_example():
    """
    Przykład użycia pakietu math.
    """
    print(math.pi) # zwraca liczbę pi
    print(math.e) # zwraca liczbę e
    print(math.tau) # zwraca liczbę tau
    print(math.inf) # zwraca liczbę nieskończoną
    print(math.nan) # zwraca liczbę NaN (Not a Number)
    print(math.log(10, 10)) # zwraca logarytm o podstawie 10 z liczby 10
    print(math.log10(10)) # zwraca logarytm o podstawie 10 z liczby 10
    print(math.log2(10)) # zwraca logarytm o podstawie 2 z liczby 10
    print(math.log1p(10)) # zwraca logarytm naturalny z liczby 10
    print(math.pow(10, 2)) # zwraca potęgę liczby 10 do potęgi 2
    print(math.sqrt(10)) # zwraca pierwiastek kwadratowy z liczby 10
    print(math.sin(10)) # zwraca sinus liczby 10
    print(math.cos(10)) # zwraca cosinus liczby 10
    print(math.tan(10)) # zwraca tangens liczby 10
    print(math.degrees(10)) # zwraca wartość w stopniach liczby 10
    print(math.radians(10)) # zwraca wartość w radianach liczby 10
    print(math.factorial(10)) # zwraca silnię liczby 10
    print(math.gcd(10, 20)) # zwraca największy wspólny dzielnik liczb 10 i 20
    print(math.isfinite(10)) # sprawdza, czy liczba 10 jest skończona
    print(math.isinf(10)) # sprawdza, czy liczba 10 jest nieskończona
    print(math.isnan(10)) # sprawdza, czy liczba 10 jest NaN
    print(math.isclose(10, 10)) # sprawdza, czy liczba 10 jest równa liczbie 10 z uwzględnieniem błędu
    print(math.isclose(10, 10.000)) # sprawdza, czy liczba 10 jest równa liczbie 10.000 z uwzględnieniem błędu

math_module_example()


def cmath_module_example():
    """
    Przykład użycia pakietu cmath.
    """
    print(cmath.sqrt(-1)) # zwraca liczbę zespoloną (1j) - w pakiecie math zwróciłoby błąd
cmath_module_example()