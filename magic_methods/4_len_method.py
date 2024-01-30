'''
4. Metoda __len__
'''

# Przykład 1 - metoda __len__ w klasie Point
class MyList:
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        return len(self.elements)

# Utworzenie obiektu klasy MyList
# my_list = MyList([1, 2, 3, 4, 5])

# Wywołanie funkcji len() na obiekcie my_list
# print(len(my_list))  # Wyświetli: 5


# Przykład 2 - metoda __len__ w klasie Sentence
class MyContainer:
    def __init__(self):
        self.elementy = []

    def dodaj_element(self, element):
        self.elementy.append(element)

    def __len__(self):
        return len(self.elementy)

# Użycie klasy
# kontener = MyContainer()
# kontener.dodaj_element(1)
# kontener.dodaj_element(2)
# kontener.dodaj_element(3)

# Wywołanie funkcji len() na obiekcie kontener
# print('Custom len: ', len(kontener))  # Wyświetli: 3


# Przykład 3 - metoda __len__ w klasie Sentence
class Sentence:
    def __init__(self, text):
        self.text = text

    def __len__(self):
        # Podział tekstu na słowa za pomocą spacji
        words = self.text.split()
        # Zwrócenie liczby słów w zdaniu
        return len(words)

# Utworzenie obiektu klasy Sentence
# sentence = Sentence("To jest przykładowe zdanie do testowania metody __len__.")
# Wywołanie funkcji len() na obiekcie sentence
# print(len(sentence))  # Wyświetli: 8


# Przykład 4 - metoda __len__ w klasie SampleText
class SampleText:
    def __init__(
            self, 
            tekst, 
            excluded_words=[]
            ):
        self.tekst = tekst
        self.excluded_words = excluded_words

    def __len__(self):
        words = self.tekst.split()
        filtered_words = [word for word in words if word not in self.excluded_words]
        return len(filtered_words)

# Przykładowe użycie
# tekst = "To jest przykładowy tekst do testowania metody __len__()"
# excluded = ["jest", "do"]
# moj_tekst = SampleText(tekst, excluded_words=excluded)
# print(len(moj_tekst))  # Wyświetli: 6, ponieważ "jest" i "do" są pominięte
