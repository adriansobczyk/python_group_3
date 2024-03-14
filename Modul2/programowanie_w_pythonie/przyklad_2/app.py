from flask import Flask, jsonify, g
import sqlite3
import os

'''
Komendy:
Dockerfile:
docker build . -t flask_with_db - budowanie obrazu z pliku Dockerfile
docker run -p 5000:5000 flask_with_db - uruchomienie kontenera z obrazem flask_with_db

Docker compose:
docker-compose build - budowanie obrazów z pliku docker-compose.yml
docker-compose up - uruchomienie kontenerów z pliku docker-compose.yml
'''
app = Flask(__name__)

# Ścieżka do pliku bazy danych SQLite
DATABASE = os.path.join(os.getcwd(), 'sqlite_db.db')

# Funkcja do uzyskania połączenia do bazy danych SQLite
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Utwórz tabelę w bazie danych SQLite, jeśli nie istnieje
def create_table():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT
                        )''')
        db.commit()

# Dodaj przykładowy rekord do bazy danych SQLite
def insert_data():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO my_table (name) VALUES ('example')")
        db.commit()

# Definicja endpointu, który zwraca dane z bazy danych SQLite
@app.route('/')
def get_data_from_sqlite():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM my_table")
        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

# Funkcja do zamykania połączenia z bazą danych SQLite
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    create_table()  # Utwórz tabelę przy uruchamianiu aplikacji
    insert_data()   # Dodaj przykładowy rekord przy uruchamianiu aplikacji
    app.run(debug=True, host='0.0.0.0')
