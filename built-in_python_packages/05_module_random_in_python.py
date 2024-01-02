'''
4. Generowanie liczb losowych (random) 
'''

import random

def random_example():
    """
    Przykłady generowania liczb losowych z zakresu lewostronnie domkniętego [0, 1).
    """
    liczba_losowa = random.random()
    return liczba_losowa

# print(random_example())


def randint_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczba_losowa = random.randint(1, 10)
    return liczba_losowa

# print(randint_example())


def choice_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczba_losowa = random.choice([1, 2, 3, 4, 5, 6])
    return liczba_losowa

# print(choice_example())


def choices_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczby_losowe = random.choices([1, 2, 3, 4, 5, 6], k=2) # k - ile liczb wylosować
    return liczby_losowe

# print(choices_example())


def weighted_multiply_example():
    """
    Przykład generowania losowej liczby z uwzględnieniem wag i zwracania wyniku pomnożonego przez wagę.
    """
    choices = [1, 2, 3, 4, 5, 6]
    weights = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]

    # Używamy random.choices i mnożymy losową liczbę przez odpowiadającą jej wagę
    chosen_number = random.choices(choices, weights)[0]
    multiplied_result = chosen_number * weights[choices.index(chosen_number)]

    return multiplied_result

# print(weighted_multiply_example())


def sample_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczby_losowe = random.sample([1, 2, 3, 4, 5, 6], 2)
    return liczby_losowe

# print(sample_example())


def shuffle_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczby = [1, 2, 3, 4, 5, 6]
    random.shuffle(liczby)
    return liczby

# print(shuffle_example())    

# if __name__ == "__main__":
#     print(random_example())
#     print(randint_example())
#     print(choice_example())
#     print(weighted_multiply_example())
#     print(sample_example())
#     print(shuffle_example())

