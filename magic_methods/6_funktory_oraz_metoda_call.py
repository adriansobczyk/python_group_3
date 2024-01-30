'''
6. Funktory oraz metoda call
'''

# Przykład 1
class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value

# Tworzymy obiekt funktora, który dodaje 5 do przekazanej wartości
# add_five = Adder(5)

# Wywołujemy obiekt funktora, działając na nim jak na funkcji
# result = add_five(10)
# print(result)  # Wynik: 15

# Możemy wywoływać obiekt funktora wielokrotnie z różnymi wartościami
# result = add_five(20)
# print(result)  # Wynik: 25


# Przykład 2
class Multiplier:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def __call__(self, value):
        return self.multiplier * value

# Tworzymy obiekt funktora, który mnoży przekazaną wartość przez 3
multiply_by_three = Multiplier(3)

# Wywołujemy obiekt funktora, działając na nim jak na funkcji
result = multiply_by_three(5)
print(result)  # Wynik: 15

# Możemy wywoływać obiekt funktora wielokrotnie z różnymi wartościami
result = multiply_by_three(8)
print(result)  # Wynik: 24
