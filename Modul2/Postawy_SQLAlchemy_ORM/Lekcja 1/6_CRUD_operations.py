from rel_one_to_many import User, Article, session

# Create

# user = User(name='Boris Johnson')
# session.add(user)
# session.commit()

# article = Article(title='Our country’s saddest day', content='Lorem ipsum...', user_id=user.id)
# session.add(article)
# session.commit()

# Read

# user = session.query(User).get(1)
# print(user.id, user.name)

# user1 = session.query(User).filter_by(name='Boris Johnson').first() # filter_by służy do filtrowania wyników na podstawie kolumny
# user2 = session.query(User).filter(User.name == 'Boris Johnson').scalar() # scalar() zwraca pierwszy wynik zapytania, jeśli nie ma wyników, zwraca None
# print(user1.id, user1.name)
# print(user2.id, user2.name)


# Update

# article = session.query(Article).get(1)
# article.content = 'Very important content for the article'
# session.add(article)
# session.commit()

# Delete

# article = session.query(Article).get(2)
# session.delete(article)
# session.commit()
