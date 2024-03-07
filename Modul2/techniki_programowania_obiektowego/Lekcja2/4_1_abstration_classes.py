'''
Klasy abstrakcyjne w Pythonie
'''

from abc import ABC, abstractmethod

# Implementacja naiwna
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Imię:", self.name)
        print("Wiek:", self.age)
        print("Ocena:", self.grade)


# student1 = Student("Adam", 18, "A")
# student1.display_info()


# Przykład klasy abstrakcyjnej
class MyBaseClass(ABC):
    @abstractmethod
    def foo(self):
        pass

class Child(MyBaseClass):
    # pass
    def foo(self):
        print("foo() wywołane")

# Sprawdźmy, czy Child spełnia wymagania MyBaseClass
# cl = Child()
# cl.foo()


# Przykład 2
# Definicja klasy abstrakcyjnej
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Implementacja konkretnej klasy dziedziczącej po klasie abstrakcyjnej
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Implementacja konkretnej klasy dziedziczącej po klasie abstrakcyjnej
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Utworzenie instancji obiektów
rectangle = Rectangle("Prostokąt", 5, 4)
circle = Circle("Koło", 3)

# Wywołanie metod dla obiektów
# print(f"Pole {rectangle.name}: {rectangle.area()}")
# print(f"Obwód {rectangle.name}: {rectangle.perimeter()}")
# print(f"Pole {circle.name}: {circle.area()}")
# print(f"Obwód {circle.name}: {circle.perimeter()}")
