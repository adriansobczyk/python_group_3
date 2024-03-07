# ------------------------ WYRAŻENIA REGEX ------------------------ #
import re

# Podstawowe wyrażenia regularne
# ^ - początek wyrazu
# $ - koniec wyrazu
# . - dowolny znak
# * - zero lub więcej wystąpień poprzedniego znaku
# \d - cyfra
# \w - dowolny znak alfanumeryczny
# \s - dowolny znak biały
# () - grupowanie
# \b - granica wyrazu
# + - jeden lub więcej wystąpień poprzedniego znaku
# {n} - dokładnie n wystąpienia poprzedniego znaku
# {n,m} - od n do m wystąpień poprzedniego znaku
# {n,} - co najmniej n wystąpień poprzedniego znaku
# {,m} - co najwyżej m wystąpień poprzedniego znaku
# ? - zero lub jedno wystąpienie poprzedniego znaku
# | - alternatywa
# [] - zbiór znaków
# [^] - negacja zbioru znaków
# \ - znak specjalny


def sample_regex():
    """
    Przykład użycia wyrażeń regularnych.
    Użyte zostały następujące znaki specjalne:
    ^ - początek wyrazu
    . - dowolny znak
    * - zero lub więcej wystąpień poprzedniego znaku
    $ - koniec wyrazu
    """
    pattern = r"^The.*USA$"
    txt = "The rain in USA"
    x = re.search(pattern, txt)
    if x:
        return "YES! We have a match!"
    else:
        return "No match"


def sample_regex_find_digits(x):
    """
    Przykład użycia wyrażeń regularnych.
    Użyte zostały następujące znaki specjalne:
    \d - cyfra
    """
    txt = "W roku 2024 planuję wydać 3 książki, 2 artykuły i 1 podręcznik."
    x = re.findall("\d", txt)
    return x


def sample_regex_to_search_date():
    """
    Przykład użycia wyrażeń regularnych do wyszukania daty
    Użyte zostały następujące znaki specjalne:
    \b - granica wyrazu
    \d - cyfra
    . - dowolny znak
    {2} - dokładnie 2 wystąpienia poprzedniego znaku
    {4} - dokładnie 4 wystąpienia poprzedniego znaku
    """
    pattern = r'\b\d{2}\.\d{2}.\d{4}\b'
    sample_text = "Urodziłem się 02.12.1950 w Warszawie."
    x = re.search(pattern, sample_text)
    extracted_date = x.group()
    return extracted_date


def sample_regex_to_extract_second_word():
    """
    Przykład użycia wyrażeń regularnych do wyszukania drugiego słowa w tekście.
    Użyte zostały następujące znaki specjalne:
    \b - granica wyrazu
    \w - dowolny znak alfanumeryczny
    + - jeden lub więcej wystąpień poprzedniego znaku
    \s - dowolny znak biały
    () - grupowanie
    """
    input_text = "Wyrażenia regularne to bardzo przydatny element w Pythonie."
    match = re.search(r'\b\w+\b\s+(\w+)', input_text)
    if match:
        return match.group(1)
    else:
        return None


def sample_regex_to_extract_n_word(n):
    """
    Przykład użycia wyrażeń regularnych do wyszukania słów z 4 literami.
    Użyte zostały następujące znaki specjalne:
    \b - granica wyrazu
    \w - dowolny znak alfanumeryczny
    {n} - dokładnie n wystąpienia poprzedniego znaku
    """
    input_text = "Wyrażenia regularne to bardzo przydatny element w Pythonie."
    words = re.findall(r'\b\w+\b', input_text)
    
    if n <= 0 or n > len(words):
        return None
    
    return words[n - 1]

def sample_regex_to_extract_integers_only():
    """
    Przykład użycia wyrażeń regularnych do wyszukania liczb całkowitych.
    Użyte zostały następujące znaki specjalne:
    \b - granica wyrazu
    \d - cyfra
    + - jeden lub więcej wystąpień poprzedniego znaku
    """
    input_text = "Cena za 1 kg jabłek to 3.99 zł."
    pattern = r'\b\d+\b'
    matches = re.findall(pattern, input_text)
    matched_integers = [int(match) for match in matches]
    return matched_integers

def sample_regext_to_extract_text_after_2_word():
    '''
    Przykład użycia wyrażeń regularnych do wyszukania tekstu po drugim słowie.
    Użyte zostały następujące znaki specjalne:
    ^ - początek wyrazu
    \S - dowolny znak nie będący znakiem białym
    + - jeden lub więcej wystąpień poprzedniego znaku
    \s - dowolny znak biały
    () - grupowanie tekstu do wyodrębnienia z całego wyrażenia
    $ - koniec wyrazu
    '''
    input_text = "Wyrażenia regularne to bardzo przydatny element w Pythonie."
    pattern = r'^\S+\s+\S+\s+(.*)$'
    match = re.search(pattern, input_text)
    if match:
        return match.group(1)
    else:
        return None


def sample_regex_to_replace_1_element():
    """
    Funkcja zastępuje wszystkie wystąpienia wzorca w tekście podanym jako argument.
    Użyta została metoda sub() z modułu re.
    """
    text = "To jest przykład 123."
    print("Oryginalny tekst:", text)
    pattern = r'\d+'  # Wzorzec dopasowujący cyfry
    replacement = 'XYZ'
    result = re.sub(pattern, replacement, text)
    return result


def replace_colors_with_black():
    # Zastosowanie re.sub na przykładzie
    text = "Samochód jest niebieski, a dom jest czerwony. Obraz jest żółty."
    print("Oryginalny tekst:", text)
    result = re.sub(r'(niebieski|czerwony|żółty)', 'czarny', text)
    return result


def sample_regex_to_replace_multiple_elements():
    text = "To jest przykład 123, a tutaj inne słowo 456."
    print("Oryginalny tekst:", text)

    patterns_and_replacements = [
        (r'\d+', 'X'), # Zastąp cyfry dowolną literą 'X'
        (r'przykład', 'example'),  # Zastąp słowo 'przykład' przez 'example'
    ]

    result = text
    for pattern, replacement in patterns_and_replacements:
        result = re.sub(pattern, replacement, result)

    return result


# if __name__ == '__main__':
    # pattern = r'\b\w{4}\b'
    # print(sample_regex(pattern))
    # print(sample_regex_find_digits())
    # print(sample_regex_to_search_date())
    # print(sample_regex_to_extract_second_word())
    # print(sample_regex_to_extract_n_word(4))
    # print(sample_regex_to_extract_integers_only())
    # print(sample_regext_to_extract_text_after_2_word())
    # print(sample_regex_to_replace_1_element())
    # print(sample_regex_to_replace_multiple_elements())
    # print(replace_colors_with_black())
