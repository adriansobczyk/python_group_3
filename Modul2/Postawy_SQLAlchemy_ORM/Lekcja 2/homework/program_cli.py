import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student

# Tworzenie silnika bazy danych
engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)

def create_student(name):
    session = Session()
    student = Student(fullname=name)
    session.add(student)
    session.commit()
    session.close()
    print(f"Student {name} został dodany.")

def list_students():
    session = Session()
    students = session.query(Student).all()
    session.close()
    print("Lista studentów:")
    for student in students:
        print(f"- {student.fullname}")

def update_student(student_id, new_name):
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.fullname = new_name
        session.commit()
        print(f"Dane studenta o id {student_id} zostały zaktualizowane.")
    else:
        print(f"Nie znaleziono studenta o id {student_id}.")
    session.close()

def remove_student(student_id):
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student o id {student_id} został usunięty.")
    else:
        print(f"Nie znaleziono studenta o id {student_id}.")
    session.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program CLI do zarządzania studentami w bazie danych.")
    parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"], help="Wybierz akcję do wykonania.")
    parser.add_argument("-n", "--name", help="Imię i nazwisko studenta.")
    parser.add_argument("-i", "--id", type=int, help="ID studenta do aktualizacji lub usunięcia.")
    args = parser.parse_args()

    if args.action == "create" and args.name:
        create_student(args.name)
    elif args.action == "list":
        list_students()
    elif args.action == "update" and args.id and args.name:
        update_student(args.id, args.name)
    elif args.action == "remove" and args.id:
        remove_student(args.id)
    else:
        print("Niepoprawne argumenty. Użyj -h lub --help, aby uzyskać pomoc.")

# Sample commands:
# python program_cli.py -a create -n "Jan Kowalski"
# python program_cli.py -a list
# python program_cli.py -a update -i 1 -n "Adam Nowak"
# python program_cli.py -a remove -i 2
