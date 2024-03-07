'''
7. Menadżer kontekstu
'''
import time
import random


# Przykład 1
class DatabaseConnection:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None

    def connect(self):
        print(f"Connecting to database: {self.database_name}")
        # Symulacja otwarcia połączenia do bazy danych
        self.connection = f"Connection to {self.database_name}"

    def close(self):
        if self.connection:
            print(f"Closing connection to database: {self.database_name}")
            # Symulacja zamknięcia połączenia do bazy danych
            self.connection = None

    def execute_query(self, query):
        if self.connection:
            print(f"Executing query: {query}")
            # Symulacja wykonania zapytania do bazy danych
        else:
            print("No connection to database!")

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

# Użycie niestandardowego menedżera kontekstu
# with DatabaseConnection("example_database") as db_connection:
#     db_connection.execute_query("SELECT * FROM users")
    # Symulacja zapytania do bazy danych

# Po opuszczeniu kontekstu menedżera, połączenie zostanie automatycznie zamknięte


# Przykład 2
class TextFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def open(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)

    def close(self):
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
            self.file = None

    def write(self, text):
        if self.file:
            print(f"Writing to file: {text}")
            self.file.write(text)
        else:
            print("File is not open!")

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

# Użycie niestandardowego menedżera kontekstu do zapisu tekstu do pliku
# with TextFile("7_sample.txt", "w") as file:
#     file.write("Hello, world!\n")
#     file.write("This is a test.")

# Po opuszczeniu kontekstu menedżera, plik zostanie automatycznie zamknięty

# Przykład 3
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed_time} seconds")


def sort_list():
    # Generowanie losowej listy liczb
    numbers = [random.randint(0, 1000) for _ in range(1000)]
    # Sortowanie listy
    sorted_numbers = sorted(numbers)
    return sorted_numbers

# Użycie menedżera kontekstu
# with Timer() as timer:
#     sorted_list = sort_list()

# Przykład 4
class DBConnection:
    def __enter__(self):
        print("Establishing DB connection")
        # Symulacja otwierania połączenia do bazy danych
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing DB connection")
        # Symulacja zamykania połączenia do bazy danych

class DBTransaction:
    def __enter__(self):
        print("Starting DB transaction")
        # Symulacja rozpoczęcia transakcji w bazie danych
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Committing DB transaction")
        # Symulacja zatwierdzania transakcji w bazie danych

# Przykład zagnieżdżonego menedżera kontekstu zarządzającego połączeniem do bazy danych i transakcją
# with DBConnection() as db_conn:
#     with DBTransaction() as db_trans:
#         # Tutaj można wykonywać operacje na bazie danych w obrębie transakcji
#         print("Performing database operations")
