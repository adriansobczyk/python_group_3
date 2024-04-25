from sqlalchemy import func
from sqlalchemy.sql.expression import desc
from models import Student, Group, Lecturer, Subject, Grade, session

# Zapytania
# 1. Znajdź 5 studentów z najwyższą średnią ocen ze wszystkich przedmiotów
top_students = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .join(Grade) \
    .group_by(Student.id) \
    .order_by(desc('avg_grade')) \
    .limit(5) \
    .all()

# 2. Znajdź studenta z najwyższą średnią ocen z określonego przedmiotu
top_student_subject = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .join(Grade) \
    .join(Subject) \
    .filter(Subject.name == 'Math') \
    .group_by(Student.id) \
    .order_by(desc('avg_grade')) \
    .first()

# 3. Znajdź średni wynik w grupach dla określonego przedmiotu
avg_grade_group = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .join(Subject) \
    .filter(Subject.name == 'Physics') \
    .scalar()

# Wyświetlanie wyników
print("1. 5 studentów z najwyższą średnią ocen ze wszystkich przedmiotów:")
print(top_students)
print("\n2. Student z najwyższą średnią ocen z przedmiotu Matematyka:")
print(top_student_subject)
print("\n3. Średni wynik w grupach dla przedmiotu Fizyka:")
print(avg_grade_group)