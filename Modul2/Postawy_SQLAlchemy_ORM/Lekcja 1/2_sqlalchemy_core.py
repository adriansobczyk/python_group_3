from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy import MetaData
from sqlalchemy.sql import select

import os
from dotenv import load_dotenv

# Wczytanie zmiennych środowiskowych z pliku .env
load_dotenv()

# Tworzenie silnika bazy danych w pamięci RAM komputera
# engine = create_engine('sqlite:///:memory:', echo=True)

# Tworzenie silnika bazy danych postgreSQL
DATABASE_URL = f'postgresql://{os.getenv("POSTGRES_USERNAME")}:{os.getenv("POSTGRES_PASSWORD")}@localhost/postgres'

print(os.getenv("POSTGRES_USERNAME"))
print(os.getenv("POSTGRES_PASSWORD"))

engine = create_engine(DATABASE_URL)

# Tworzenie obiektu MetaData do zarządzania tabelami
metadata = MetaData()

# Tworzenie tabeli users
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
              )

# Tworzenie tabeli addresses
addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )

# Tworzenie tabel w bazie danych za pomocą obiektu MetaData
metadata.create_all(engine)

# Wstawianie danych do tabeli users za pomocą obiektu insert i metody values
ins = users.insert().values(name='jack', fullname='Jack Jones')
print(str(ins))

# Wykonanie zapytania SQL na bazie danych za pomocą metody connect i metody execute
with engine.connect() as conn:
    # Wykonanie zapytania SQL na bazie danych
    result = conn.execute(ins)
    # Tworzenie zapytania SQL na bazie danych za pomocą metody select
    s = select(users)
    # Wykonanie zapytania SQL na bazie danych za pomocą metody execute
    result = conn.execute(s)
    # Zatwierdzenie zmian w bazie danych
    # conn.commit()
    # Iteracja po wynikach zapytania SQL i wyświetlenie ich na konsoli za pomocą pętli for
    for row in result:
        print(row)  # (1, u'jack', u'Jack Jones')