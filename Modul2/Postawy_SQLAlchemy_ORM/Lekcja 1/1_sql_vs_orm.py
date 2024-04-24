'''
SQL vs ORM (Object-Relational Mapping)
'''

from sqlite3 import Error, connect

# Przykładowy kod tworzący bazę danych SQLite3

def create_connection(db_file):
    conn = None
    try:
        conn = connect(db_file)
        print(f"Connected to {db_file}")
    except Error as e:
        print(e)
    return conn


def create_projects_table(conn):
    try:
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS projects (
                id integer PRIMARY KEY,
                name text NOT NULL,
                begin_date text,
                end_date text
            );"""
        )
    except Error as e:
        print(e)


def create_tasks_table(conn):
    try:
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS tasks (
                id integer PRIMARY KEY,
                name text NOT NULL,
                priority integer,
                project_id integer NOT NULL,
                status_id integer NOT NULL,
                begin_date text NOT NULL,
                end_date text NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            );"""
        )
    except Error as e:
        print(e)


def main():
    conn = connect('pythonsqlite_raw_sql.db')
    create_projects_table(conn)
    create_tasks_table(conn)
    conn.close()


if __name__ == '__main__':
    main()


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
# Tworzenie silnika bazy danych
'''

Parametry create_engine

url (string): Adres URL bazy danych. Może to być adres lokalny, adres zdalny lub adres bazy danych w pamięci.
echo (bool): Określa, czy generowane zapytania SQL mają być wydrukowywane na konsoli. Wartość True oznacza wydrukowanie zapytań, co jest przydatne do debugowania. Domyślnie ustawione na False.
pool_size (int): Określa maksymalną liczbę połączeń w puli połączeń do bazy danych. Domyślnie ustawione na 5.
max_overflow (int): Określa maksymalną liczbę dodatkowych połączeń, które mogą zostać utworzone, gdy pulia połączeń jest już w pełni wykorzystana. Domyślnie ustawione na 10.
pool_timeout (int): Określa maksymalny czas oczekiwania (w sekundach) na uzyskanie połączenia z puli połączeń przed zgłoszeniem błędu. Domyślnie ustawione na 30.
pool_recycle (int): Określa czas (w sekundach), po którym połączenie w puli zostanie zrecyklowane, co oznacza zamknięcie i ponowne otwarcie połączenia w celu zapobieżenia problemom z połączeniem. Ustawienie wartości na -1 oznacza, że recykling jest wyłączone. Domyślnie ustawione na -1.
pool_pre_ping (bool): Określa, czy przed każdym zapytaniem do bazy danych ma być wysyłane pingowanie w celu sprawdzenia, czy połączenie jest nadal aktywne. Domyślnie ustawione na False.
connect_args (dict): Dodatkowe argumenty przekazywane do funkcji połączenia z bazą danych, które mogą być używane do konfiguracji połączenia na poziomie sterownika bazy danych.
execution_options (dict): Opcje wykonania, które mogą być przekazane do metod wykonania zapytania, takie jak izolacja transakcji, optymalizacja zapytań itp.
'''

engine = create_engine('sqlite:///pythonsqlite_orm.db', echo=True)


# Deklaracja bazy
Base = declarative_base() # klasa bazowa dla wszystkich klas modeli ORM w aplikacji SQLAlchemy

# Definicja modelu projektu
class Project(Base):
    __tablename__ = 'projects' # nazwa tabeli w bazie danych

    id = Column(Integer, primary_key=True) # kolumna identyfikatora projektu (klucz główny) o typie Integer (liczba całkowita)
    name = Column(String, nullable=False) # kolumna nazwy projektu o typie String (tekst) i wymagana (nie może być pusta)
    begin_date = Column(Date) # kolumna daty rozpoczęcia projektu o typie Date (data)
    end_date = Column(Date)

# Definicja modelu zadania
class Task(Base):
    __tablename__ = 'tasks' # nazwa tabeli w bazie danych

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    priority = Column(Integer)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False) # klucz obcy do tabeli projektów (projects) na podstawie kolumny id (klucz główny) w tabeli projektów (projects) i wymagany (nie może być pusty)
    status_id = Column(Integer, nullable=False)
    begin_date = Column(Date, nullable=False, default=datetime.datetime.now())
    end_date = Column(Date, nullable=False)

# Tworzenie schematu bazy danych
'''
Jest to metoda obiektu MetaData lub Base w SQLAlchemy, która tworzy wszystkie tabele zdefiniowane w modelach ORM na podstawie 
obiektów tabeli. Można go wywołać na obiekcie MetaData lub Base razem z silnikiem bazy danych. Ta metoda jest używana do utworzenia 
wszystkich tabel w bazie danych na podstawie zdefiniowanych modeli ORM.
'''
Base.metadata.create_all(engine)

# Tworzenie sesji
'''
Jest to funkcja, która tworzy fabrykę sesji. Przyjmuje argumenty, takie jak silnik bazy danych, klasa sesji, klasa transakcji itp., 
i zwraca funkcję, która może być używana do tworzenia nowych sesji. Jest to użyteczne, ponieważ pozwala uniknąć powtarzania kodu 
do tworzenia sesji i ułatwia zarządzanie sesjami w aplikacji.
'''
Session = sessionmaker(bind=engine)


'''
Jest to klasa reprezentująca sesję w SQLAlchemy. Może być utworzona poprzez wywołanie fabryki sesji zwróconej przez sessionmaker. 
Sesja jest używana do wykonywania operacji na bazie danych, takich jak dodawanie, modyfikowanie, usuwanie i pobieranie danych. 
Umożliwia również zarządzanie transakcjami, śledzenie zmian i zarządzanie połączeniem z bazą danych.
'''
session = Session()
