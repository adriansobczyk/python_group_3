'''
12. Nadpisywanie operacji porównywania

__eq__(self, other): Definiuje zachowanie równości obiektów (==).
__ne__(self, other): Definiuje zachowanie nierówności obiektów (!=).
__lt__(self, other): Definiuje zachowanie mniejszości obiektu względem innego obiektu (<).
__le__(self, other): Definiuje zachowanie mniejszości lub równości obiektu względem innego obiektu (<=).
__gt__(self, other): Definiuje zachowanie większości obiektu względem innego obiektu (>).
__ge__(self, other): Definiuje zachowanie większości lub równości obiektu względem innego obiektu (>=).
'''

# Przykład 1 - porównywanie obiektów
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.distance_from_origin() == other.distance_from_origin()

    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Przykład użycia
# p1 = Point(3, 4)
# p2 = Point(1, 2)
# p3 = Point(3, 4)

# print(p1 == p2)  # False
# print(p1 == p3)  # True
# print(p1 < p2)   # False
# print(p2 < p3)   # True

# Przykład 2 - porównywanie obiektów
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return len(self.title) < len(other.title)

    def __str__(self):
        return f"{self.title} by {self.author}"

# Przykład użycia
# book1 = Book("Python Crash Course", "Eric Matthes", 562)
# book2 = Book("Clean Code", "Robert C. Martin", 464)
# book3 = Book("Python Cookbook", "David Beazley", 706)

# print(book1 == book2)  # False - różne tytuły
# print(book1 == book3)  # False - różne tytuły
# print(book1 < book2)   # True - długość tytułu "Python Crash Course" jest mniejsza niż "Clean Code"
# print(book2 < book3)   # False - długość tytułu "Clean Code" jest większa niż "Python Cookbook"
# print(book1)           # Python Crash Course by Eric Matthes


# Przykład 3 - porównywanie obiektów
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

    def __lt__(self, other):
        # Porównujemy owoce alfabetycznie po nazwie
        return self.name < other.name

    def __str__(self):
        return f"{self.color} {self.name}"

# Użycie
apple = Fruit("Apple", "Red")
orange = Fruit("Orange", "Orange")
banana = Fruit("Banana", "Yellow")

print(apple == orange)  # False
print(apple == Fruit("Apple", "Red"))  # True
print(banana < orange)   # True

# fruits = [apple, orange, banana]
# fruits.sort()
# print([str(fruit) for fruit in fruits])  # ['Yellow Banana', 'Red Apple', 'Orange Orange']
