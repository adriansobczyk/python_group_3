'''
Przykładowy kod łączący dwie tabele w  synchronicznym SQLAlchemy ORM
'''

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine("sqlite:///joins_in_ORM.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    articles = relationship('Article', back_populates='author')


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer(), primary_key=True)
    title = Column(String(255))
    content = Column(Text())
    user_id = Column(Integer(), ForeignKey('users.id'))
    author = relationship('User', back_populates='articles')


Base.metadata.create_all(engine)

user1 = User(name='John')
user2 = User(name='Alice')

article1 = Article(title='First Article', content='Content of the first article', author=user1)
article2 = Article(title='Second Article', content='Content of the second article', author=user2)
article3 = Article(title='Third Article', content='Content of the third article', author=user1)

session.add_all([user1, user2, article1, article2, article3])
session.commit()

# Wykonaj zapytanie JOIN, aby uzyskać wszystkie artykuły wraz z nazwami autorów
articles_with_authors = session.query(Article.title, User.name)\
                               .join(User, Article.user_id == User.id)\
                               .all()

# Wyświetl wyniki zapytania
for article, author in articles_with_authors:
    print(f"Article: {article} | Author: {author}")