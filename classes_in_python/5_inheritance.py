'''
5 . Dziedziczenie  - ponowne użycie klasy na podstawie innej klasy 
'''

# Przykład 1
class Animal:
    def ruch(self):
        print("Zwierze porusza się")

class Bird(Animal):
    def latanie(self):
        print("Ptak fruwa")

class Mammal(Animal):
    def karmienie(self):
        print("Ssak karmi się mlekiem")

# Przykłady dziedziczenia:
# orzel = Bird()
# orzel.ruch()  # Odziedziczone od Zwierze
# orzel.latanie()  # Odziedziczone od Ptak

# kot = Mammal()
# kot.ruch()  # Odziedziczone od Zwierze
# kot.karmienie()  # Odziedziczone od Ssak


# Metoda Resolution Order (MRO)
# print(Bird.__mro__)  # lub Bird.mro()

# Przykład 2

class ProgrammingLanguage:
   def __init__(self, name, typing, level):
       self.name = name
       self.typing = typing
       self.level = level
 
   def __str__(self):
       return f"{self.name}, {self.typing}, {self.level}"


class Python(ProgrammingLanguage):
    def __init__(self, name="Python", typing="Dynamic", level="High"):
        super().__init__(name, typing, level)


class Java(ProgrammingLanguage):
    def __init__(self, name="Java", typing="Static", level="High"):
        super().__init__(name, typing, level)


# jezyk1 = Python()
# print(jezyk1)
# jezyk2 = Java()
# print(jezyk2)
# jezyk3 = ProgrammingLanguage("C#", "Static", "High")
# print(jezyk3)
        

# Przykład 3
class Person:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Person):
    def __init__(self, imie, nazwisko, numer_indeksu):
        super().__init__(imie, nazwisko) # super jest 
        self.numer_indeksu = numer_indeksu

    def studiuj(self):
        print(f"{self.imie} {self.nazwisko} studiuje")


class Lecturer(Person):
    def __init__(self, imie, nazwisko, przedmiot):
        super().__init__(imie, nazwisko)
        self.przedmiot = przedmiot

    def wykladaj(self):
        print(f"{self.imie} {self.nazwisko} wyklada przedmiot: {self.przedmiot}")


class College:
    def __init__(self, lecturer, student):
        self.lecturer = lecturer
        self.student = student

    def wyklad(self):
        print(f"Wykładowca {self.lecturer.imie} {self.lecturer.nazwisko} wykłada przedmiot {self.lecturer.przedmiot} studentowi {self.student.imie} {self.student.nazwisko} z numerem indeksu {self.student.numer_indeksu}")

# Przykład użycia:
# student1 = Student("Jan", "Kowalski", "12345")
# student1.studiuj()
# wykladowca1 = Lecturer("Profesor", "Nowak", "Informatyka")
# wykladowca1.wykladaj()
# lecturer = Lecturer("Jan", "Kowalski", "Matematyka")
# student = Student("Anna", "Nowak", 123456)
# college = College(lecturer, student)
# college.wyklad()
