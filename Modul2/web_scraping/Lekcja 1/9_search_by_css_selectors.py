import requests
from bs4 import BeautifulSoup

'''
Wyszukiwanie według selektorów CSS
'''

url = "http://quotes.toscrape.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

'''
Proste selektory
'''
# znaleźć pierwszy znacznik <p> na stronie
p = soup.select("p")
# print(p)

text = soup.select(".text")
# print(text)

header = soup.select("#header")
# print(header)

'''
Selektory kombinowane
'''

a = soup.select("div.container a")
# print(a)

'''
Atrybuty
'''

href = soup.select("[href^='https://']")
# print(href)
