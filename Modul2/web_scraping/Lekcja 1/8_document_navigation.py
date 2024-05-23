import requests
from bs4 import BeautifulSoup

'''
Nawigacja po dokumencie
'''

url = "http://quotes.toscrape.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# znaleźć pierwszy znacznik <p> na stronie
first_paragraph = soup.find("p")
# print(first_paragraph)

'''
Elementy podrzędne
'''

body_children = list(first_paragraph.children)
# print(body_children)

# znaleźć pierwszy znacznik <a> wewnątrz pierwszego znacznika <div> na stronie
first_div = soup.find("div")
first_div_link = first_div.find("a")
# print(first_div_link)

'''
Elementy nadrzędne
'''

first_paragraph_parent = first_paragraph.parent
# print(first_paragraph_parent)

container = soup.find("div", attrs={"class": "quote"}).find_parent("div", class_="col-md-8")
# print(container)

'''
Sąsiadujące elementy
'''

next_sibling = soup.find("span", attrs={"class": "tag-item"}).find_next_sibling("span")
# print(next_sibling)

previous_sibling = next_sibling.find_previous_sibling("span")
print(previous_sibling)

