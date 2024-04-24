from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')
DBSession = sessionmaker(bind=engine) # tworzy fabrykę sesji o nazwie DBSession, która bedzie tworzyć sesje połączone z silnikiem engine
session = DBSession() # Tworzy nową sesję bazy danych o nazwie session, korzystając z fabryki sesji DBSession. Teraz możemy użyć tej sesji do wykonywania operacji na bazie danych, takich jak dodawanie, modyfikowanie i pobieranie danych.

print(DBSession)