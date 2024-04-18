'''
Przykładowy kod metod z modułu PEP 249
'''

import sqlite3


def connect_to_database(database_name):
    # Połączenie z bazą danych SQLite
    conn = sqlite3.connect(database_name)
    return conn


def create_cursor(connection):
    # Uzyskanie obiektu kursora
    cursor = connection.cursor()
    return cursor


def create_table(cursor, table_name, columns):
    # Utworzenie tabeli
    query = f'CREATE TABLE {table_name} ({columns})'
    cursor.execute(query)


def insert_data(cursor, table_name, data):
    # Wstawienie danych do tabeli
    query = f'INSERT INTO {table_name} VALUES ({data})'
    cursor.execute(query)
    cursor.connection.commit() # Konieczne dla zapisu zmian w bazie danych


def execute_query(cursor, query):
    # Wykonanie zapytania SQL
    cursor.execute(query)


def execute_many_queries(cursor, query, data):
    # Wykonanie wielu zapytań SQL
    cursor.executemany(query, data)


def fetch_single_record(cursor):
    # Pobranie pojedynczego rekordu wyniku
    row = cursor.fetchone()
    return row


def fetch_all_records(cursor):
    # Pobranie wszystkich rekordów wyniku
    rows = cursor.fetchall()
    return rows


# Przykładowe wywołanie funkcji
conn = connect_to_database('example.db')
cursor = create_cursor(conn)
# create_table(cursor, 'example_table', 'id INTEGER PRIMARY KEY, name TEXT')
# insert_data(cursor, 'example_table', '1, "Alice"')
# insert_data(cursor, 'example_table', '2, "Bob"')
# insert_data(cursor, 'example_table', '3, "Charlie"')  
  
sample_query = execute_query(cursor, 'SELECT * FROM example_table')
# print(sample_query)
row = fetch_single_record(cursor)
print("Single record: ", row)
rows = fetch_all_records(cursor)
print("All records: ", rows) # Fetchall nie zwróci pierwszego, rekordu jeżeli już został pobrany przez fetchone
cursor.close()
conn.close()