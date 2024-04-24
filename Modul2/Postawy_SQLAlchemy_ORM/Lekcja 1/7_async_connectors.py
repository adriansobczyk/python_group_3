import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

import os
from dotenv import load_dotenv
# Utwórz silnik asynchroniczny
# engine = create_async_engine('sqlite+aiosqlite:///sqlalchemy_example.db')

# Wczytaj zmienne środowiskowe
load_dotenv()

# Utwórz silnik postgreSQL asynchroniczny
DATABASE_URL = f'postgresql+asyncpg://{os.getenv("POSTGRES_USERNAME")}:{os.getenv("POSTGRES_PASSWORD")}@localhost/postgres'
engine = create_async_engine(DATABASE_URL)

# Deklaruj model
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)


# Funkcja asynchroniczna do tworzenia tabel w bazie danych
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Funkcja asynchroniczna do dodawania użytkownika do bazy danych
async def add_user():
    async with AsyncSession(engine) as session:
        async with session.begin():
            new_user = User(name='jack', fullname='Jack Jones')
            session.add(new_user)
            await session.commit()


# Uruchomienie operacji asynchronicznych
async def main():
    await create_tables()  # Najpierw utwórz tabele
    await add_user()       # Następnie dodaj użytkownika

asyncio.run(main())
