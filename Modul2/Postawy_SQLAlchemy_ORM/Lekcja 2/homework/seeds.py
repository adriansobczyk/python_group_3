from faker import Faker
import random
from models import Student, Group, Lecturer, Subject, Grade, session


# Tworzenie danych testowych za pomocą Faker
fake = Faker()

# Dodawanie studentów
for _ in range(30):
    student = Student(fullname=fake.name())
    session.add(student)

# Dodawanie grup
groups = ['Group A', 'Group B', 'Group C']
for group_name in groups:
    group = Group(name=group_name)
    session.add(group)

# Dodawanie przedmiotów i przypisywanie wykładowców
lecturers = []
for _ in range(3):
    lecturer = Lecturer(fullname=fake.name())
    session.add(lecturer)
    lecturers.append(lecturer)

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Computer Science']
for subject_name, lecturer in zip(subjects, lecturers):
    subject = Subject(name=subject_name, lecturer=lecturer)
    session.add(subject)

# Dodawanie ocen dla studentów
for student in session.query(Student):
    for subject in session.query(Subject):
        for _ in range(random.randint(0, 20)):
            grade = Grade(student=student, subject=subject, grade=random.randint(2, 5))
            session.add(grade)

# Zapisywanie zmian w bazie danych
session.commit()