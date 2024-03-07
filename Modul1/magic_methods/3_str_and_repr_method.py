'''
3. Metoda __str__
'''

# Przykład 1 - metoda __str__ w klasie Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point(x={self.x}, y={self.y})'

# Utworzenie obiektu klasy Point
# point = Point(3, 5)
# print(str(point))  # Wywołanie metody __str__() i wyświetlenie reprezentacji tekstowej obiektu


# Przykład 2 - metoda __str__ w klasie Employee
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

# Utworzenie obiektów reprezentujących pracowników
# employee1 = Employee("John Doe", "Software Developer", 60000)
# employee2 = Employee("Jane Smith", "Project Manager", 80000)

# Wyświetlenie informacji o pracownikach za pomocą metody __str__()
# print(employee1)  # Name: John Doe, Position: Software Developer, Salary: $60000
# print(employee2)  # Name: Jane Smith, Position: Project Manager, Salary: $80000

# Przykład 3 - metoda __str__ oraz dziedziczenie
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"To jest klasa nadrzędna, wartość: {self.value}"

class SubClass(MyClass):
    def __str__(self):
        return f"To jest klasa dziedzicząca, wartość: {self.value}"


# Przykładowe użycie:
# obj1 = MyClass(5)
# obj2 = SubClass(10)

# print(obj1)
# print(obj2)

'''
4. Metoda __repr__
'''

# Przykład 1 - metoda __repr__ w klasie Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Utworzenie obiektu klasy Point
# point = Point(3, 4)

# Wywołanie metody __repr__() na obiekcie
# print(repr(point))  # Point(3, 4)


# Przykład 2 - metoda __repr__ w klasie Employee
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"Employee(name={self.name}, position={self.position}, salary={self.salary})"

# Utworzenie obiektów reprezentujących pracowników
employee1 = Employee("John Doe", "Software Developer", 60000)
employee2 = Employee("Jane Smith", "Project Manager", 80000)

# Wyświetlenie informacji o pracownikach za pomocą metody __repr__()
print(employee1)  # Employee(name=John Doe, position=Software Developer, salary=60000)
print(employee2)  # Employee(name=Jane Smith, position=Project Manager, salary=80000)