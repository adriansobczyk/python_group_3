from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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
    begin_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)