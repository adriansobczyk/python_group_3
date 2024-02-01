'''
11. Zastępowanie operatorów matematycznych

__add__: dodawanie
__sub__: odejmowanie
__mul__: mnożenie
__truediv__: dzielenie
__floordiv__: dzielenie całkowite
__mod__: reszta z dzielenia
__pow__: potęgowanie
__neg__: negacja (unarny minus)
__pos__: operator dodatni (unarny plus)
'''

# Przykład 1 - dodawanie
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Użycie
# point1 = Point(2, 3)
# point2 = Point(4, 5)
# sum_point = point1 + point2
# print("Suma punktów:", sum_point.x, sum_point.y)  # Suma punktów: 6 8


# Przykład 2 - odejmowanie
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

# Użycie
# point1 = Point(2, 3)
# point2 = Point(4, 5)
# diff_point = point1 - point2
# print("Różnica punktów:", diff_point.x, diff_point.y)  # Różnica punktów: -2 -2


# Przykład 3 - mnożenie
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

# Użycie
# point1 = Point(2, 3)
# scaled_point = point1 * 2
# print("Wynik mnożenia przez skalar:", scaled_point.x, scaled_point.y)  # Wynik mnożenia: 4 6


# Przykład 4 - dzielenie
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

# Użycie
# point2 = Point(4, 5)
# divided_point = point2 / 2
# print("Wynik dzielenia przez skalar:", divided_point.x, divided_point.y)  # Wynik dzielenia przez skalar: 2.0 2.5


# Przykład 5 - potęgowanie'
class Point:
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y

    def __pow__(self, power):
        return Point(self.x ** power, self.y ** power)

# Użycie
# point1 = Point(2, 3)
# powered_point = point1 ** 2
# print("Wynik potęgowania punktu:", powered_point.x, powered_point.y)  # Wynik potęgowania punktu: 4 9
