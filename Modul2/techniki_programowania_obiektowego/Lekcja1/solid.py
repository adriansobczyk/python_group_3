'''
Zasady projektowania SOLID
'''

# Single Responsibility Principle (Zasada pojedynczej odpowiedzialności)
# Przykład 1
class Calculator:
    def add(self, x, y):
        return x + y

class Logger:
    def log(self, message):
        # Logika logowania
        print(message)

# calculator = Calculator()
# result = calculator.add(3, 5)
# logger = Logger()
# logger.log(f"Result: {result}")


# Przykład 2
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        # Metoda odpowiedzialna za odczyt pliku
        with open(self.file_name, 'r') as file:
            data = file.read()
        return data

    def write_file(self, data):
        # Metoda odpowiedzialna za zapis danych do pliku
        with open(self.file_name, 'w') as file:
            file.write(data)


class DataManager:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def process_data(self):
        # Metoda odpowiedzialna za przetwarzanie danych
        data = self.file_manager.read_file()
        # Przetwarzanie danych...
        processed_data = data.upper()


# file_name = "data.txt"
# file_manager = FileManager(file_name)
# data_manager = DataManager(file_manager)
# data_manager.process_data()

# Open/Closed Principle (Zasada otwarte-zamknięte)
from abc import ABC, abstractmethod

# Przykład 1
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# rectangle = Rectangle(3, 4)
# circle = Circle(5)
# print("Rectangle area:", rectangle.area())
# print("Circle area:", circle.area())


# Przykład 2
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Hau Hau"

class Cat(Animal):
    def sound(self):
        return "Meow"

class AnimalSound:
    def __init__(self, animal):
        self.animal = animal

    def make_sound(self):
        return self.animal.sound()

# dog = Dog()
# cat = Cat()
# dog_sound = AnimalSound(dog)
# print("Dog says:", dog_sound.make_sound())
# cat_sound = AnimalSound(cat)
# print("Cat says:", cat_sound.make_sound())


# Liskov Substitution Principle (Zasada podstawienia Liskov):
# Przykład 1
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostrich cannot fly")

# sparrow = Sparrow()
# ostrich = Ostrich()
# sparrow.fly()
# ostrich.fly()
    
# Przykład 2
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Funkcja, która przyjmuje obiekt typu Shape
def calculate_area(shape):
    return shape.area()

# rectangle = Rectangle(4, 6)
# square = Square(5)
# print("Area of rectangle:", calculate_area(rectangle))
# print("Area of square:", calculate_area(square))



# Interface Segregation Principle (Zasada segregacji interfejsów)
# Przykład 1
class Printer(ABC):
    @abstractmethod
    def print_content(self, content: str) -> None:
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_content(self, content: str) -> None:
        pass

# Implementacje interfejsów

class SimplePrinter(Printer):
    def print_content(self, content: str) -> None:
        print(f"Printing: {content}")

class SimpleScanner(Scanner):
    def scan_content(self, content: str) -> None:
        print(f"Scanning: {content}")

class Photocopier(Printer, Scanner):
    def print_content(self, content: str) -> None:
        print(f"Printing: {content}")

    def scan_content(self, content: str) -> None:
        print(f"Scanning: {content}")

# Klient korzystający z interfejsów

class User:
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner

    def perform_tasks(self):
        self.printer.print_content("Sample Document")
        self.scanner.scan_content("Sample Document")

# Tworzymy instancje i wykorzystujemy je w kliencie

# printer = SimplePrinter()
# scanner = SimpleScanner()
# photocopier = Photocopier()
# user1 = User(printer, scanner)
# user1.perform_tasks()
# user2 = User(photocopier, photocopier)
# user2.perform_tasks()

# Przykład 2
class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass

# Implementacje interfejsów

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self) -> float:
        return 2 * 3.14 * self.radius

# Klient korzystający z interfejsów

class AreaCalculator:
    def __init__(self, shape: Shape):
        self.shape = shape

    def calculate_area(self) -> float:
        return self.shape.calculate_area()

class PerimeterCalculator:
    def __init__(self, shape: Shape):
        self.shape = shape

    def calculate_perimeter(self) -> float:
        return self.shape.calculate_perimeter()

# Tworzymy instancje i wykorzystujemy je w kliencie
# rectangle = Rectangle(5, 4)
# circle = Circle(3)
# area_calculator = AreaCalculator(rectangle)
# print("Area of rectangle:", area_calculator.calculate_area())
# perimeter_calculator = PerimeterCalculator(rectangle)
# print("Perimeter of rectangle:", perimeter_calculator.calculate_perimeter())
# area_calculator_circle = AreaCalculator(circle)
# print("Area of circle:", area_calculator_circle.calculate_area())
# perimeter_calculator_circle = PerimeterCalculator(circle)
# print("Perimeter of circle:", perimeter_calculator_circle.calculate_perimeter())


# Dependency Inversion Principle (Zasada odwrócenia zależności):
# Przykład 1
class DatabaseConnection:
    def connect(self):
        # Logika łączenia z bazą danych
        print("Connected to the database")

class FileManager:
    def read_file(self):
        # Logika odczytu pliku
        print("Reading file")

class DataProcessor:
    def process_data(self, data_source):
        data_source.process()

class DatabaseConnectionAdapter:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def process(self):
        self.db_connection.connect()
        # Logika przetwarzania danych z bazy danych
        print("Processing data from database")

class FileManagerAdapter:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def process(self):
        self.file_manager.read_file()
        # Logika przetwarzania danych z pliku
        print("Processing data from file")

# Użycie odwrócenia zależności:
# database_connection = DatabaseConnection()
# db_adapter = DatabaseConnectionAdapter(database_connection)
# data_processor_db = DataProcessor()
# data_processor_db.process_data(db_adapter)
# file_manager = FileManager()
# file_adapter = FileManagerAdapter(file_manager)
# data_processor_file = DataProcessor()
# data_processor_file.process_data(file_adapter)


# Przykład 2
# Abstrakcyjna klasa bazowa
class Messenger(ABC):
    @abstractmethod
    def send_message(self, message: str) -> None:
        pass


# Klasa implementująca wysyłanie wiadomości przez email
class EmailMessenger(Messenger):
    def send_message(self, message: str) -> None:
        print("Sending email:", message)

# Klasa implementująca wysyłanie wiadomości przez SMS
class SMSMessenger(Messenger):
    def send_message(self, message: str) -> None:
        print("Sending SMS:", message)

# Klasa aplikacji, która wysyła wiadomość
class NotificationService:
    def __init__(self, messenger: Messenger):
        self.messenger = messenger

    def send_notification(self, message: str) -> None:
        self.messenger.send_message(message)

# # Użycie aplikacji do wysyłania wiadomości przez email
email_messenger = EmailMessenger()
notification_service_email = NotificationService(email_messenger)
notification_service_email.send_notification("Hello! This is an email notification.")
# Użycie aplikacji do wysyłania wiadomości przez SMS
sms_messenger = SMSMessenger()
notification_service_sms = NotificationService(sms_messenger)
notification_service_sms.send_notification("Hello! This is an SMS notification.")
