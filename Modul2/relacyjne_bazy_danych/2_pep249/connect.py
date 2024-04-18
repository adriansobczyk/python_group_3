import sqlite3
from contextlib import contextmanager

database = './test.db' # ścieżka do pliku bazy danych

@contextmanager
def create_connection(db_file):  # Deklaracja funkcji create_connection z argumentem db_file
    """ create a database connection to a SQLite database """  # Tworzenie połączenia z bazą danych SQLite
    conn = sqlite3.connect(db_file)  # Utwórz połączenie z bazą danych
    yield conn  # Zwróć połączenie
    conn.rollback()  # Wycofaj zmiany
    conn.close()  # Zamknij połączenie
