'''
8. Iteratory i generatory
'''

# Przykład iteratora
# my_list = [1, 2, 3, 4]
# my_iter = iter(my_list)

# print(next(my_iter))  # Wydrukuj pierwszy element
# print(next(my_iter))  # Wydrukuj drugi element
# print(next(my_iter))  # Wydrukuj trzeci element


# Tworzenie iteratora - przykład 1
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

# even_iter = EvenNumbers(10)
# for num in even_iter:
#     print(num)


# Tworzenie iteratora - przykład 2
class Vowels:
    def __init__(self, word):
        self.word = word
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        vowels = 'aeiouAEIOU' # samogłoski
        while self.index < len(self.word):
            if self.word[self.index] in vowels:
                current_vowel = self.word[self.index]
                self.index += 1
                return current_vowel
            self.index += 1
        raise StopIteration

# Użycie iteratora
# word_iter = Vowels('Hello World')
# for vowel in word_iter:
#     print(vowel)


# Tworzenie iteratora - przykład 3
class LineReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    yield line.strip()  # Zwraca odczytaną linię bez znaku nowej linii
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found")

# Użycie klasy z generatorem do odczytu pliku linia po linii
# file_path = '9_example.txt'
# line_reader = LineReader(file_path)
# for line in line_reader:
#     print(line)



# Tworzenie generatora - przykład 1
def custom_iterator(max_value):
    current_value = 0
    while current_value < max_value:
        yield current_value
        current_value += 1

# c = custom_iterator(10)
# for i in c:
#     print(i)


# Tworzenie generatora - przykład 2
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Użycie generatora
# fib = fibonacci_generator()
# for _ in range(700):
#     print(next(fib))


# Tworzenie generatora - przykład 3
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Użycie generatora
# for i in countdown(500):
#     print(i)
