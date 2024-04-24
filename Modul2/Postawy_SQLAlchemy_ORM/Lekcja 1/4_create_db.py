from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship(Person)


Base.metadata.create_all(engine)
Base.metadata.bind = engine


new_person = Person(name="Bill")
session.add(new_person)

session.commit()

new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()


for person in session.query(Person).all():
    print(f'Person: id: {person.id}, name: {person.name}')

for address in session.query(Address).all():
    print(f'Address: id: {address.id}, post code: {address.post_code}, person: {address.person.name}')