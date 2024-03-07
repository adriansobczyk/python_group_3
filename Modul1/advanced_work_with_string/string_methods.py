# ------------------------ METODY CIĄGÓW ZNAKÓW ------------------------ #

def capitalize_string_method():
    '''
    Metoda capitalize() - zwraca kopię ciągu znaków, w której pierwsza litera jest wielka, a pozostałe małe
    '''
    string = 'to jest przykład stringa'
    capitalized_string = string.capitalize()
    return capitalized_string


def lower_string_method():
    '''
    Metoda lower() - zwraca kopię ciągu znaków, w której wszystkie litery są małe
    '''
    string = 'TO JEST PRZYKŁAD STRINGA'
    lower_string = string.lower()
    return lower_string


def upper_string_method():
    '''
    Metoda upper() - zwraca kopię ciągu znaków, w której wszystkie litery są duże
    '''
    string = 'to jest przykład stringa'
    upper_string = string.upper()
    return upper_string


def swapcase_string_method():
    '''
    Metoda swapcase() - zwraca kopię ciągu znaków, w której wszystkie litery są zamienione na przeciwne (małe na duże, duże na małe)
    '''
    string = 'To Jest Przykład Stringa'
    swapcase_string = string.swapcase()
    return swapcase_string


def title_string_method():
    '''
    Metoda title() - zwraca kopię ciągu znaków, w której wszystkie słowa zaczynają się wielką literą
    '''
    string = 'to jest przykład stringa'
    title_string = string.title()
    return title_string


def center_string_method():
    '''
    Metoda center() - zwraca kopię ciągu znaków, w której oryginalny ciąg znaków jest wyśrodkowany
    '''
    string = 'to jest przykład stringa'
    center_string = string.center(50)
    return center_string


def strip_string_method():
    '''
    Metoda strip() - zwraca kopię ciągu znaków, w której usunięto wszystkie białe znaki z początku i końca ciągu znaków
    '''
    string = '    to jest przykład stringa'
    print("Przed: ", string)
    strip_string = string.strip()
    return strip_string


def lstrip_string_method():
    '''
    Metoda lstrip() - zwraca kopię ciągu znaków, w której usunięto wszystkie białe znaki z początku ciągu znaków
    '''
    string = '    to jest przykład stringa    '
    lstrip_string = string.lstrip()
    return lstrip_string


def rstrip_string_method():
    '''
    Metoda rstrip() - zwraca kopię ciągu znaków, w której usunięto wszystkie białe znaki z końca ciągu znaków
    '''
    string = '    to jest przykład stringa    '
    rstrip_string = string.rstrip()
    return rstrip_string


def replace_string_method():
    '''
    Metoda replace() - zwraca kopię ciągu znaków, w której wszystkie wystąpienia podciągu znaków zostały zastąpione innym podciągiem znaków
    '''
    string = 'to jest przykład stringa.'
    print("Przed: ", string)
    replace_string = string.replace('stringa', 'ciągu znaków')
    return replace_string


def split_string_method():
    '''
    Metoda split() - zwraca listę ciągów znaków, w której oryginalny ciąg znaków został podzielony na podciągi znaków
    '''
    string = 'to jest przykład stringa'
    split_string = string.split()
    return split_string


def split_string_method_with_separator():
    '''
    Metoda split() - zwraca listę ciągów znaków, w której oryginalny ciąg znaków został podzielony na podciągi znaków
    '''
    string = 'to jest przykład stringa'
    split_string = string.split(' ', 2)
    return split_string


def join_string_method():
    '''
    Metoda join() - zwraca ciąg znaków, w którym wszystkie elementy sekwencji zostały połączone
    '''
    string = 'to jest przykład stringa'
    split_string = string.split()
    print("Przed: ", split_string)
    join_string = ' '.join(split_string)
    return join_string


def find_string_method():
    '''
    Metoda find() - zwraca indeks pierwszego wystąpienia podciągu znaków w ciągu znaków
    '''
    string = 'to jest przykład stringa'
    find_string = string.find('przykład')
    return find_string


def rfind_string_method():
    '''
    Metoda rfind() - zwraca indeks ostatniego wystąpienia podciągu znaków w ciągu znaków
    '''
    string = 'to jest przykład stringa'
    rfind_string = string.rfind('a')
    return rfind_string



def count_string_method():
    '''
    Metoda count() - zwraca liczbę wystąpień podciągu znaków w ciągu znaków
    '''
    string = 'to jest przykład stringa'
    count_string = string.count('a')
    return count_string


def startswith_string_method():
    '''
    Metoda startswith() - zwraca True, jeśli ciąg znaków zaczyna się od podciągu znaków, w przeciwnym razie zwraca False
    '''
    string = 'to jest przykład stringa'
    startswith_string = string.startswith('to')
    return startswith_string


def endswith_string_method():
    '''
    Metoda endswith() - zwraca True, jeśli ciąg znaków kończy się podciągiem znaków, w przeciwnym razie zwraca False
    '''
    string = 'to jest przykład stringa'
    endswith_string = string.endswith('stringa')
    return endswith_string


def isalnum_string_method():
    '''
    Metoda isalnum() - zwraca True, jeśli wszystkie znaki w ciągu znaków są alfanumeryczne (a-z, A-Z, 0-9), w przeciwnym razie zwraca False
    '''
    string = 'to jest przykład stringa'
    isalnum_string = string.isalnum()
    return isalnum_string


def isalpha_string_method():
    '''
    Metoda isalpha() - zwraca True, jeśli wszystkie znaki w ciągu znaków są alfabetyczne (a-z, A-Z), w przeciwnym razie zwraca False
    '''
    string = 'to jest przykład stringa'
    isalpha_string = string.isalpha()
    return isalpha_string


def isdigit_string_method():
    '''
    Metoda isdigit() - zwraca True, jeśli wszystkie znaki w ciągu znaków są cyframi (0-9), w przeciwnym razie zwraca False
    '''
    string = 'to jest przykład stringa'
    isdigit_string = string.isdigit()
    return isdigit_string


def islower_string_method():
    '''
    Metoda islower() - zwraca True, jeśli wszystkie znaki w ciągu znaków są małe, w przeciwnym razie zwraca False
    '''
    string = 'to jest przykład stringa'
    islower_string = string.islower()
    return islower_string


def isspace_string_method():
    '''
    Metoda isspace() - zwraca True, jeśli wszystkie znaki w ciągu znaków są białe, w przeciwnym razie zwraca False
    '''
    string = 'to jest przykład stringa'
    isspace_string = string.isspace()
    return isspace_string


def istitle_string_method():
    '''
    Metoda istitle() - zwraca True, jeśli wszystkie słowa w ciągu znaków zaczynają się wielką literą, w przeciwnym razie zwraca False
    '''
    string = 'To Jest Przykład Stringa'
    istitle_string = string.istitle()
    return istitle_string


def isupper_string_method():
    '''
    Metoda isupper() - zwraca True, jeśli wszystkie znaki w ciągu znaków są duże, w przeciwnym razie zwraca False
    '''
    string = 'TO JEST PRZYKŁAD STRINGA'
    isupper_string = string.isupper()
    return isupper_string

import string
def has_special_characters():
    '''
    Funkkcja has_special_characters() - zwraca True, jeśli ciąg znaków zawiera znaki specjalne, w przeciwnym razie zwraca False
    '''
    my_string = "Hello! How are you?"
    special_characters = string.punctuation
    print(special_characters)

    return any(char in special_characters for char in my_string)


def removeprefix_string_method():
    '''
    Metoda removeprefix() - zwraca kopię ciągu znaków, w której usunięto podany prefiks
    '''
    string = 'to jest przykład stringa'
    removeprefix_string = string.removeprefix('to')
    return removeprefix_string


def removesuffix_string_method():
    '''
    Metoda removesuffix() - zwraca kopię ciągu znaków, w której usunięto podany sufiks
    '''
    string = 'to jest przykład stringa'
    removesuffix_string = string.removesuffix('stringa')
    return removesuffix_string


# if __name__ == '__main__':
    # print(capitalize_string_method())
    # print(lower_string_method())
    # print(upper_string_method())
    # print(swapcase_string_method())
    # print(title_string_method())
    # print(center_string_method())
    # print(strip_string_method())
    # print(lstrip_string_method())
    # print(rstrip_string_method())
    # print(replace_string_method())
    # print(split_string_method())
    # print(split_string_method_with_separator())
    # print(join_string_method())
    # print(find_string_method())
    # print(rfind_string_method())
    # print(count_string_method())
    # print(startswith_string_method())
    # print(endswith_string_method())
#     print(isalnum_string_method())
#     print(isalpha_string_method())
    # print(isdigit_string_method())
    # print(islower_string_method())
    # print(isspace_string_method())
#     print(istitle_string_method())
#     print(isupper_string_method())
    # print(has_special_characters())
    # print(removeprefix_string_method())
    # print(removesuffix_string_method())
