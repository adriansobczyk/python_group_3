'''
3. Atrybuty klasy (pola i metody)
'''

class SampleClass:
    # Atrybuty klasy
    name = "Pole klasy"

    # Metody klasy
    def sample_method(self): #  “self” to parametr odnoszący się do instancji klasy
        print("Metoda klasy")
    
    def sample_calculation(self, a, b):
        return a + b


obiekt_klasy = SampleClass()
print(obiekt_klasy.name)
obiekt_klasy.sample_method()
print(obiekt_klasy.sample_calculation(2, 3))


class Animal:
    name = "Ares"
    weight = 10

    def noise(self):
        noise = "Hau hau"
        return noise

    # Metoda zmieniająca wartość atrybutu name
    def change_name(self, new_name):
        self.name = new_name
        return self.name


# Utworzenie instancji klasy Animal
animal = Animal()
print(animal.name)
print(animal.weight)
print(animal.noise())
print(animal.change_name("Burek"))
print(animal.name)