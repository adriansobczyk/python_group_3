'''
6. Polimorfizm (polymorphism) - pozwala na wykonywanie tej samej operacji na różnych typach danych.
'''

# Przykład 1
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Funkcja przyjmująca obiekt Animal i wywołująca jego metodę sound
def make_sound(animal):
    animal.sound()

# Tworzenie różnych obiektów i wywoływanie metody sound
# dog = Dog()
# cat = Cat()

# make_sound(dog)  # Wywoła "Bark"
# make_sound(cat)  # Wywoła "Meow"


# Przykład 2
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()


# Przykład 3
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Funkcja obliczająca obszar dla różnych kształtów
def calculate_shape_area(shape):
    return shape.calculate_area()

# Tworzenie różnych kształtów i obliczanie ich obszarów
rectangle = Rectangle(5, 4)
circle = Circle(3)

# print("Obszar prostokąta:", calculate_shape_area(rectangle))  # Wywoła 20
# print("Obszar koła:", calculate_shape_area(circle))  # Wywoła około 28.26
