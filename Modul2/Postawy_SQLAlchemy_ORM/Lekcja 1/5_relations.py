
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
DBSession = sessionmaker(bind=engine)
session = DBSession()

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
user = User(name='Peter Miller')
article = Article(title='Our country’s saddest day', content='Today is our country’s saddest day')
user.articles.append(article)
session.add(user)
session.commit()

users= session.query(User).filter_by(name='Peter Miller').all()

for user in users:
    for article in user.articles:
        print(article.title, user.name)

article = session.query(Article).filter_by(title='Our country’s saddest day').one()
print(article.title, article.author.name)



