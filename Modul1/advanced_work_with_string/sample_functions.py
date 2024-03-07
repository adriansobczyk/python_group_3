import string


def find_locations(locations_dict, key, letter_case=False):
    """
    Funkcja wyszukuje lokalizacje w słowniku na podstawie podanego klucza.

    :param locations_dict: Lista słowników reprezentujących lokalizacje.
    :param key: Kombinacja do wyszukania w miastach lub państwach.
    :param letter_case: Określa, czy w wyszukiwaniu rozróżniana jest wielkość liter (domyślnie False).
    :return: Lista słowników zawierających pasujące lokalizacje, gdzie klucze to 'miasto', 'panstwo', 'kontynent'.
    """
    results = []

    for location in locations_dict:
        # Dostosowanie kluczy i wartości
        city = location['miasto']
        country = location['panstwo']
        continent = location['kontynent']

        # Dostosowanie wielkości liter, jeśli wymagane
        if not letter_case:
            city = city.lower()
            country = country.lower()
            continent = continent.lower()
            key = key.lower()

        # Sprawdzenie, czy klucz występuje w mieście lub państwie
        if key in city or key in country or key in continent:
            results.append({
                'miasto': location['miasto'],
                'panstwo': location['panstwo'],
                'kontynent': location['kontynent']
            })

    return results


def sanitize_numbers_with_replace(numbers):
    """
    Funkcja normalizuje liczby, usuwając znaki (, -, ), + i spacje, pozostawiając jedynie cyfry.

    :param numbers: Numer telefonu w różnych formatach.
    :return: Znormalizowany numer telefonu, zawierający jedynie cyfry.
    """
    # Usuwanie znaków specjalnych
    numbers = numbers.replace('(', '')
    numbers = numbers.replace(')', '')
    numbers = numbers.replace('-', '')
    numbers = numbers.replace('+', '')
    numbers = numbers.replace(' ', '')

    
    return numbers


def run_sanitization_with_replace(sample_numbers):
    """
    Funkcja uruchamia normalizację numerów telefonów z użyciem funkcji sanitize_numbers_with_replace.
    """
    sanitized_numbers = []
    for numer in sample_numbers:
        wynik = sanitize_numbers_with_replace(numer)
        sanitized_numbers.append(wynik)
    
    return sanitized_numbers


def sanitize_numbers(numbers):
    """
    Funkcja normalizuje liczby, usuwając znaki (, -, ), + i spacje, pozostawiając jedynie cyfry.

    :param numbers: Numer telefonu w różnych formatach.
    :return: Znormalizowany numer telefonu, zawierający jedynie cyfry.
    """
    # Inicjalizacja pustego ciągu do przechowywania cyfr
    digits_only = ""

    # Iteracja po znakach w numerze telefonu
    for char in numbers:
        # Dodawanie cyfr do ciągu tylko wtedy, gdy są cyframi
        if char.isdigit():
            digits_only += char

    return digits_only


def check_if_contains_text(text, key):
    """
    Funkcja sprawdza, czy podany klucz występuje w tekście.

    :param text: Tekst do sprawdzenia.
    :param key: Klucz do wyszukania.
    :return: True, jeśli klucz występuje w tekście, w przeciwnym wypadku False.
    """
    if key in text:
        return True
    else:
        return False


def find_duplicated_elements(list_of_elements):
    zduplikowane = set()
    unikalne = set()

    for elem in list_of_elements:
        if elem in unikalne:
            zduplikowane.add(elem)
        else:
            unikalne.add(elem)

    return list(zduplikowane)


def escape_characters(text):
    """
    Funkcja zamienia znaki specjalne na ich reprezentację tekstową.

    :param text: Tekst do zamiany.
    :return: Tekst z zamienionymi znakami specjalnymi.
    """
    # Zamiana znaków specjalnych na ich reprezentację tekstową
    text = text.replace("\n", "\\n")
    text = text.replace("\r", "\\r")
    text = text.replace("\t", "\\t")
    text = text.replace("\b", "\\b")
    text = text.replace("\f", "\\f")
    text = text.replace("\'", "\\'")
    text = text.replace("\"", "\\\"")
    return text


# if __name__ == '__main__':
    # lokalizacje_dict = [
    #     {'miasto': 'Nowy Jork', 'panstwo': 'USA', 'kontynent': 'Ameryka Północna'},
    #     {'miasto': 'Paryż', 'panstwo': 'Francja', 'kontynent': 'Europa'},
    #     {'miasto': 'Tokio', 'panstwo': 'Japonia', 'kontynent': 'Azja'},
    # ]

    # # Przykładowe użycie funkcji find_locations
    # sample_key = "tokio"
    # wynik = find_locations(lokalizacje_dict, sample_key)
    # print(wynik)

    # Przykładowe użycie funkcji sanitize_numbers
    # sample_numbers = [
    #     "+-yv(080)348-78-8",
    #     "     0503451234",
    #     "050123456tu7",
    # ]
    # print(run_sanitization_with_replace(sample_numbers))

#     # Przykładowe użycie funkcji sanitize_numbers
    # sample_numbers = [
    #     "+-yv(050)348-78-8",
    #     "     0503451234",
    #     "050123456tu7",
    # ]
    # print("Przed:", sample_numbers)

    # for numer in sample_numbers:
    #     wynik = sanitize_numbers(numer)
    #     print(wynik)

#     # Przykładowe użycie funkcji check_if_contains_text
    # sample_text = "To jest przykładowy tekst"
    # sample_key = "tekst"
    # print(check_if_contains_text(sample_text, sample_key))

#     # Przykładowe użycie funkcji find_duplicated_elements
    # sample_list = ['jabłko', 'gruszka', 'banan', 'jabłko', 'banan', 'pomarańcza', 'gruszka']
    # print(find_duplicated_elements(sample_list))
    # joined_list = ', '.join(find_duplicated_elements(sample_list))
    # print(joined_list)

    # print("To jest tekst z \n nową linią")
    # print(escape_characters("To jest tekst z \n nową linią"))