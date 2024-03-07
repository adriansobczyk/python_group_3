'''
Wzorce projektowe w Pythonie
'''

from abc import ABC, abstractmethod

# FABRYKA ABSTRAKCYJNA

# Interfejsy abstrakcyjne dla produktów
class Shape:
    def draw(self):
        pass

class Color:
    def fill(self):
        pass

# Implementacje produktów
class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")

class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")

class Red(Color):
    def fill(self):
        print("Inside Red::fill() method.")

class Blue(Color):
    def fill(self):
        print("Inside Blue::fill() method.")

# Fabryka abstrakcyjna
class AbstractFactory:
    def get_color(self, color):
        pass

    def get_shape(self, shape):
        pass

# Fabryka produktów dla kształtów
class ShapeFactory(AbstractFactory):
    def get_shape(self, shape_type):
        if shape_type == 'Circle':
            return Circle()
        elif shape_type == 'Square':
            return Square()
        else:
            return None

# Fabryka produktów dla kolorów
class ColorFactory(AbstractFactory):
    def get_color(self, color_type):
        if color_type == 'Red':
            return Red()
        elif color_type == 'Blue':
            return Blue()
        else:
            return None

# Fabryka produkcji fabryk
class FactoryProducer:
    @staticmethod
    def get_factory(factory_type):
        if factory_type == 'Shape':
            return ShapeFactory()
        elif factory_type == 'Color':
            return ColorFactory()
        else:
            return None

# Pobierz fabrykę kształtów
# shape_factory = FactoryProducer.get_factory('Shape')
# Pobierz konkretny kształt z fabryki kształtów
# circle = shape_factory.get_shape('Circle')
# circle.draw()
# Pobierz fabrykę kolorów
# color_factory = FactoryProducer.get_factory('Color')
# Pobierz konkretny kolor z fabryki kolorów
# red = color_factory.get_color('Red')
# red.fill()

# METODA WYTWÓRCZA

# Interfejs Produktu
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Konkretne produkty
class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation."

class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation."

# Interfejs Fabryki
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result

# Konkretne fabryki
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Użycie wzorca Metoda Wytwórcza
# creator_a = ConcreteCreatorA()
# print(creator_a.some_operation())
# creator_b = ConcreteCreatorB()
# print(creator_b.some_operation())


# SINGELTON
class Singleton:
    _instance = None

    def __new__(cls): # cls odnosi się do klasy, która jest obecnie tworzona lub obsługiwana
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Przykład użycia Singletona
# Tworzenie instancji Singletona
s1 = Singleton()
s2 = Singleton()

# Sprawdzanie, czy obiekt s1 i s2 są tym samym Singletonem
print(s1 is s2)  # Output: True