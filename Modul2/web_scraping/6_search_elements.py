import requests
from bs4 import BeautifulSoup

'''
Praca z zawartością elementów
'''

url = "http://quotes.toscrape.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# znaleźć pierwszy znacznik <p> na stronie
first_paragraph = soup.find("p")
# print(first_paragraph)

# znaleźć wszystkie znaczniki <p> na stronie
all_paragraphs = soup.find_all("p")
# print(all_paragraphs)

