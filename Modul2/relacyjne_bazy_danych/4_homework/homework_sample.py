'''
Przykład wykonania zadania domowego
'''

from faker import Faker
import random
import sqlite3

fake = Faker()


class CreateConnection:
    '''
    Klasa do tworzenia połączenia z bazą danych. Przyjmuje nazwę bazy danych. 
    Połączenie jest otwierane w momencie utworzenia obiektu.
    '''
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name) # Stworzenie połączenia z bazą danych
        self.cur = self.conn.cursor() # Stworzenie kursora do bazy danych. Kursor to obiekt, który pozwala na wykonywanie poleceń SQL na bazie danych.

    def close_connection(self):
        self.conn.close() # Zamknięcie połączenia z bazą danych
        print("Connection closed.")
    
    # Metody __enter__ i __exit__ są wykorzystywane w kontekście with.
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback() # Rollback w przypadku wystąpienia błędu
        else:
            self.conn.commit() # Zatwierdzenie zmian w bazie danych
        self.conn.close()
        print("Connection closed.")


class CreateTables:
    '''
    Klasa do tworzenia tabel w bazie danych. Przyjmuje obiekt połączenia.
    W konstruktorze tworzone są tabele students, groups, lecturers, subjects, grades.
    '''
    def __init__(self, connection):
        self.conn = connection # Przypisanie obiektu połączenia do zmiennej
        self.cur = connection.cur # Przypisanie kursora do zmiennej

    def create_tables(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            group_id INTEGER)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS groups (
                            id INTEGER PRIMARY KEY,
                            name TEXT)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS lecturers (
                            id INTEGER PRIMARY KEY,
                            name TEXT)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS subjects (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            lecturer_id INTEGER,
                            FOREIGN KEY (lecturer_id) REFERENCES lecturers(id))''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS grades (
                            id INTEGER PRIMARY KEY,
                            student_id INTEGER,
                            subject_id INTEGER,
                            grade INTEGER,
                            date TEXT,
                            FOREIGN KEY (student_id) REFERENCES students(id),
                            FOREIGN KEY (subject_id) REFERENCES subjects(id))''')


class InsertData:
    '''
    Klasa do wstawiania danych do bazy danych. Przyjmuje obiekt połączenia.
    Metoda generate_fake_data generuje dane do wstawienia.
    Metoda insert_fake_data wstawia dane do bazy danych.
    '''
    def __init__(self, connection):
        self.conn = connection
        self.cur = connection.cur

    def insert_group(self, name):
        self.cur.execute("INSERT INTO groups (name) VALUES (?)", (name,)) # Wstawienie danych do tabeli groups w bazie danych (nazwa grupy) 
        self.conn.conn.commit() # Zatwierdzenie zmian w bazie danych (zapisanie zmian). W przypadku wstawiania danych do bazy danych, zmiany nie są zapisywane automatycznie.
        return self.cur.lastrowid # Zwrócenie ID ostatniego wstawionego rekordu w celu ewentualnego wykorzystania w innych miejscach programu

    def insert_student(self, name, group_id):
        self.cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))
        self.conn.conn.commit()
        return self.cur.lastrowid

    def insert_lecturer(self, name):
        self.cur.execute("INSERT INTO lecturers (name) VALUES (?)", (name,))
        self.conn.conn.commit()
        return self.cur.lastrowid

    def insert_subject(self, name, lecturer_id):
        self.cur.execute("INSERT INTO subjects (name, lecturer_id) VALUES (?, ?)", (name, lecturer_id))
        self.conn.conn.commit()
        return self.cur.lastrowid

    def insert_grade(self, student_id, subject_id, grade, date):
        self.cur.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)", (student_id, subject_id, grade, date))
        self.conn.conn.commit()

    def generate_fake_data(self):
        groups = ['Group A', 'Group B', 'Group C']
        lecturers = [fake.name() for _ in range(5)]
        subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History']
        students = [(fake.name(), random.choice(groups)) for _ in range(30)] # Wybór losowej grupy dla studenta z listy grup

        grades = []
        for student in students:
            for subject in subjects:
                for _ in range(random.randint(5, 20)): # Wygenerowanie losowej liczby ocen z przedziału 5-20
                    grade = random.randint(1, 6) # Wygenerowanie losowej oceny z przedziału 1-6
                    date = fake.date_this_year(before_today=True, after_today=False) # Wygenerowanie losowej daty w tym roku
                    grades.append((student[0], subject, grade, date)) # Dodanie oceny do listy ocen

        return groups, lecturers, subjects, students, grades # Zwrócenie wygenerowanych danych w postaci krotek

    def insert_fake_data(self):
        groups, lecturers, subjects, students, grades = self.generate_fake_data() # Wygenerowanie danych do wstawienia do bazy danych

        # Insert groups
        group_ids = {} # Słownik do przechowywania ID grup
        for group in groups:
            group_id = self.insert_group(group) # Wstawienie grupy do bazy danych i zapisanie ID
            group_ids[group] = group_id # Dodanie ID grupy do słownika

        # Insert lecturers
        lecturer_ids = {}
        for lecturer in lecturers:
            lecturer_id = self.insert_lecturer(lecturer)
            lecturer_ids[lecturer] = lecturer_id

        # Insert subjects
        subject_ids = {}
        for subject, lecturer_id in zip(subjects, lecturer_ids.values()): # Iteracja po dwóch listach jednocześnie (subjects i lecturer_ids.values()) za pomocą funkcji zip
            subject_id = self.insert_subject(subject, lecturer_id) # Wstawienie przedmiotu do bazy danych
            subject_ids[subject] = subject_id # Dodanie ID przedmiotu do słownika

        # Insert students
        student_ids = {}
        for student, group in students:
            student_id = self.insert_student(student, group_ids[group]) # Wstawienie studenta do bazy danych z przypisaniem do grupy (group_ids[group])
            student_ids[student] = student_id

        # Insert grades
        for grade in grades:
            student_id = student_ids[grade[0]]
            subject_id = subject_ids[grade[1]]
            self.insert_grade(student_id, subject_id, grade[2], grade[3].strftime('%Y-%m-%d'))


class DisplayData:
    '''
    Klasa do wyświetlania danych z bazy danych. Przyjmuje obiekt połączenia.
    Metody display_students, display_groups, display_lecturers, display_subjects, display_grades
    wyświetlają dane z odpowiednich tabel.
    '''
    def __init__(self, connection):
        self.conn = connection
        self.cur = connection.cur

    def display_students(self):
        self.cur.execute("SELECT * FROM students") # Wykonanie zapytania SQL do bazy danych (pobranie wszystkich rekordów z tabeli students)
        students = self.cur.fetchall() # Pobranie wyników zapytania do zmiennej students (rezultat zapytania to lista krotek)
        for student in students:
            print("Student data:")
            print("Student ID:", student[0]) # Wyświetlenie ID studenta (pierwszy element krotki)
            print("Name:", student[1]) # Wyświetlenie imienia studenta (drugi element krotki)
            print("Group ID:", student[2]) # Wyświetlenie ID grupy studenta (trzeci element krotki)
            print("----------------------")

    def display_groups(self):
        self.cur.execute("SELECT * FROM groups")
        groups = self.cur.fetchall()
        for group in groups:
            print("Group data:")
            print("Group ID:", group[0])
            print("Name:", group[1])
            print("----------------------")

    def display_lecturers(self):
        self.cur.execute("SELECT * FROM lecturers")
        lecturers = self.cur.fetchall()
        for lecturer in lecturers:
            print("Lecturer data:")
            print("Lecturer ID:", lecturer[0])
            print("Name:", lecturer[1])
            print("----------------------")

    def display_subjects(self):
        self.cur.execute("SELECT * FROM subjects")
        subjects = self.cur.fetchall()
        for subject in subjects:
            print("Subject data:")
            print("Subject ID:", subject[0])
            print("Name:", subject[1])
            print("Lecturer ID:", subject[2])
            print("----------------------")

    def display_grades(self):
        self.cur.execute("SELECT * FROM grades")
        grades = self.cur.fetchall()
        for grade in grades:
            print("Grade data:")
            print("Grade ID:", grade[0])
            print("Student ID:", grade[1])
            print("Subject ID:", grade[2])
            print("Grade:", grade[3])
            print("Date:", grade[4])
            print("----------------------")


def main():
    # Utworzenie połączenia z bazą danych
    connection = CreateConnection("university.db")

    # Stworzenie tabel w bazie danych
    create_tables = CreateTables(connection)
    create_tables.create_tables()

    # Dodanie danych do bazy danych
    insert_data = InsertData(connection)
    insert_data.insert_fake_data()

    # Wyświetlenie danych z bazy danych
    display_data = DisplayData(connection)
    display_data.display_students()
    # display_data.display_groups()
    # display_data.display_lecturers()
    # display_data.display_subjects()
    # display_data.display_grades()

    # Zamknięcie połączenia z bazą danych
    connection.close_connection()


def main_with_context():
    with CreateConnection("university.db") as connection:
        create_tables = CreateTables(connection)
        create_tables.create_tables()

        insert_data = InsertData(connection)
        insert_data.insert_fake_data()

        display_data = DisplayData(connection)
        display_data.display_students()
        # display_data.display_groups()
        # display_data.display_lecturers()
        # display_data.display_subjects()
        # display_data.display_grades()

def execute_sql_query(query_file_path, parameters=None):
    # Read SQL query from file
    with open(query_file_path, 'r') as query_file:
        query = query_file.read()

    # Execute SQL query
    with sqlite3.connect("university.db") as conn:
        cursor = conn.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
    print(result)

    return result


if __name__ == "__main__":
    # main()
    main_with_context()
    query_result = execute_sql_query("query_1.sql")
