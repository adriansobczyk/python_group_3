import sqlite3

def create_db():
# odczyt pliku ze skryptem służącym do utworzenia bazy danych
    with open('salary.sql', 'r') as f:
        sql = f.read()

# tworzenie połączenia z bazą danych (jeśli plik bazy danych nie istnieje, zostanie on utworzony)
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
# uruchomienie skryptu z pliku, który utworzy tabele w bazie danych
        cur.executescript(sql)

if __name__ == "__main__":
    create_db()
