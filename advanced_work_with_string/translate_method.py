# ------------------------ METODA TRANSLATE ------------------------ #

# Metoda translate() służy do tłumaczenia znaków w łańcuchu znaków.
# Przyjmuje ona jeden argument - słownik, w którym klucze to znaki, które mają być zamienione,
# a wartości to znaki, na które mają być zamienione.


def custom_translate(input_text):
    custom_mapping = {72: 69}  # Mapping 'H' to 'E'
    translated_text = input_text.translate(custom_mapping)
    return translated_text


def sample_translate_function(input_string):
    # Utwórz słownik mapowania znaków
    translation_dict = {'a': '1',
                         'b': '2', 
                         'c': '3', 
                         'd': '4', 
                         'e': '5',
                         't': '8'
                         }

    # Użyj metody translate do zamiany znaków zgodnie z zdefiniowanym słownikiem
    translated_string = input_string.translate(str.maketrans(translation_dict))
    return translated_string


def ascii_to_polish(input_text):
    # Zdefiniuj słownik mapowania znaków
    ascii_chars = "AaCcEeLlNnOoSsZz"
    polish_chars = "ĄąĆćĘęŁłŃńÓóŚśŻż"

    translation_table = str.maketrans(
        ascii_chars,
        polish_chars
    )

    # Użyj metody translate do zamiany znaków zgodnie z zdefiniowanym słownikiem
    result_text = input_text.translate(translation_table)

    return result_text



def replace_ascii_with_translate(string):
    """
    Funkcja zamienia znaki ASCII na znaki z polskimi znakami diakrytycznymi.
    """
    # Utworzenie słownika zamienników
    replacements = {
        # Małe litery
        'a': 'ą',
        'c': 'ć',
        'e': 'ę',
        'l': 'ł',
        'n': 'ń',
        'o': 'ó',
        's': 'ś',
        'z': 'ż',
        'x': 'ź',
        # Duże litery
        'A': 'Ą',
        'C': 'Ć',
        'E': 'Ę',
        'L': 'Ł',
        'N': 'Ń',
        'O': 'Ó',
        'S': 'Ś',
        'Z': 'Ż',
        'X': 'Ź'
    }

    # Zamiana znaków z użyciem metody translate()
    for key, value in replacements.items():
        string = string.translate(string.maketrans(key, value))

    return string


def run_replace_ascii_with_translate():
    """
    Funkcja uruchamia zamianę znaków ASCII na znaki z polskimi znakami diakrytycznymi.
    """
    # Przykładowy łańcuch znaków
    string = 'To jest przykład łańcucha znaków z polskimi znakami diakrytycznymi'

    # Zamiana znaków
    string = replace_ascii_with_translate(string)

    return string


def convert_to_polish(russian_name, russian_surname):
    '''
    Funkcja zamienia imię i nazwisko zapisane cyrylicą na imię i nazwisko zapisane polskimi znakami.
    Używa metody translate() oraz str.maketrans() do zamiany znaków zgodnie z zdefiniowanym słownikiem.
    '''
    cyrillic_letters = "АБВГДЭФГХИЙКЛМНОПРСТУВЩЬЫЗ"
    polish_letters = "ABVGDEFGHIJKLMNOPRSTUVWXYZ"
    translation_table = str.maketrans(cyrillic_letters, polish_letters)
    polish_name = russian_name.translate(translation_table)
    polish_surname = russian_surname.translate(translation_table)
    return polish_name, polish_surname


# if __name__ == '__main__':
    # my_text = "Hello Sam!"
    # print(my_text)
    # result = custom_translate(my_text)
    # print(result)

    # input_text = "test"
    # result = sample_translate_function(input_text)
    # print(result)

    # ascii_text = "Hello World!"
    # polish_text = ascii_to_polish(ascii_text)
    # print(f"Original ASCII Text: {ascii_text}")
    # print(f"Converted to Polish: {polish_text}")

    # print(run_replace_ascii_with_translate())

    # russian_name = "ЕЛЕНА"
    # russian_surname = "ФЕДОРОВ"  # Replace with the actual surname
    # polish_name, polish_surname = convert_to_polish(russian_name, russian_surname)

    # print("Original Name and Surname:", russian_name, russian_surname)
    # print("Polish Name and surname:", polish_name, polish_surname)