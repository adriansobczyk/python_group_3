import requests
from bs4 import BeautifulSoup

'''
Wyszukiwanie elementów
'''

url = "http://quotes.toscrape.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# znaleźć pierwszy znacznik <p> na stronie
first_paragraph = soup.find("p")

# uzyskać tekst pierwszego znacznika <p> na stronie
first_paragraph_text = first_paragraph.get_text()
print(first_paragraph_text.strip())# 'Login'

# uzyskać wartość atrybutu "href" pierwszego znacznika <a> na stronie
first_link = soup.find("a")
first_link_href = first_link["href"]
print(first_link_href)# '/'