'''
4. Generowanie liczb losowych (random) 
'''

from random import randrange, random, randint, choice, choices, sample, shuffle 

def random_example():
    """
    Przykłady generowania liczb losowych z zakresu lewostronnie domkniętego [0, 1).
    """
    liczba_losowa = random()
    return liczba_losowa

# print(random_example())


def randint_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczba_losowa = randint(1, 10)
    return liczba_losowa

# print(randint_example())


def choice_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczba_losowa = choice([1, 2, 3, 4, 5, 6])
    return liczba_losowa

# print(choice_example())


def choices_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczby_losowe = choices([1, 2, 3, 4, 5, 6], k=2) # k - ile liczb wylosować
    return liczby_losowe

# print(choices_example())


def weighted_multiply_example():
    """
    Przykład generowania losowej liczby z uwzględnieniem wag i zwracania wyniku pomnożonego przez wagę.
    """
    my_choices = [1, 2, 3, 4, 5, 6]
    weights = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]

    # Używamy random.choices i mnożymy losową liczbę przez odpowiadającą jej wagę
    chosen_number = choices(my_choices, weights)[0]
    multiplied_result = chosen_number * weights[my_choices.index(chosen_number)]

    return multiplied_result

# print(weighted_multiply_example())


def sample_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczby_losowe = sample([1, 2, 3, 4, 5, 6], 2)
    return liczby_losowe

# print(sample_example())


def shuffle_example():
    """
    Przykłady generowania liczb losowych.
    """
    liczby = [1, 2, 3, 4, 5, 6]
    shuffle(liczby)
    return liczby

# print(shuffle_example())

def get_list_of_numbers(min_val=1, max_val=15, quantity=4):
    '''
    Funkcja generuje listę unikalnych liczb losowych w porządku rosnącym.

    :param min_val: minimalna wartość liczby losowej
    :param max_val: maksymalna wartość liczby losowej
    :param quantity: ilość liczb losowych
    
    :return: lista unikalnych liczb losowych w porządku rosnącym
    '''
    # Sprawdź czy warunki ograniczeń parametrów funkcji zostały naruszone
    # min_val jest mniejsze od max_val i quantity jest większe od min_val i mniejsze od max_val
    if not (1 <= min_val < max_val <= 1000 and min_val < quantity < max_val): 
        return "Parametry nie spełniają warunków."

    numbers = [randrange(min_val, max_val) for _ in range(quantity)]
    
    return numbers

# print(get_list_of_numbers(1, 12, 4))


def generate_random_professions(input_dict, quantity=9):
    if len(input_dict) < quantity:
        raise ValueError("Liczba wybranych kluczy nie może być większa niż liczba dostępnych kluczy w słowniku.")
    # Losowo wybierz określoną ilość kluczy
    selected_keys = choices(list(input_dict.keys()), k=quantity)
    # Losowo wybierz określoną ilość kluczy z unikalnymi wartościami
    unique_keys = sample(list(input_dict.keys()), k=quantity)
    # Twórz listę par klucz-wartość z wybranymi kluczami i losowymi profesjami
    result_list = [(key, input_dict[key]) for key in selected_keys]
    return selected_keys

# input_data = {
#     "Anna": "Inżynier",
#     "Marcin": "Nauczyciel",
#     "Katarzyna": "Lekarz",
#     "Piotr": "Artysta",
#     "Alicja": "Programista"
# }
# print(generate_random_professions(input_data))

# if __name__ == "__main__":
#     print(random_example())
#     print(randint_example())
#     print(choice_example())
#     print(weighted_multiply_example())
#     print(sample_example())
#     print(shuffle_example())
#     print(get_list_of_numbers(1, 12, 4))
