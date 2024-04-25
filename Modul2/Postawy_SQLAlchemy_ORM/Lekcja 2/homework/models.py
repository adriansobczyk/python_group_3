from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import select
from sqlalchemy.sql.expression import desc
from faker import Faker
import random
from datetime import datetime

# Tworzenie silnika bazy danych
engine = create_engine('sqlite:///school.db')
Base = declarative_base()


# Definicja modeli SQLAlchemy
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    grades = relationship("Grade", order_by="Grade.date_received", back_populates="student")

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Lecturer(Base):
    __tablename__ = 'lecturers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    subjects = relationship("Subject", order_by="Subject.name", back_populates="lecturer")

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lecturer_id = Column(Integer, ForeignKey('lecturers.id'))
    lecturer = relationship("Lecturer", back_populates="subjects")
    grades = relationship("Grade", order_by="Grade.date_received", back_populates="subject")

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date_received = Column(DateTime, default=datetime.now)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")

Base.metadata.create_all(engine)
Base.metadata.bind = engine

# Tworzenie sesji SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()