# ------------------------ ZAAWANSOWANE TWORZENIE CIĄGU ZNAKÓW ------------------------ #

def sample_string_creation():
    '''
    Przykłady tworzenia ciągu znaków
    '''
    string = 'To jest string'
    return string


def samle_unicode_string_creation():
    '''
    Przykłady tworzenia ciągu znaków z użyciem znaku u (unicode).
    W Pythonie 3.x wszystkie stringi są unicode, więc nie ma potrzeby używania znaku u.
    '''
    unicode_string = u"hi there!"
    return unicode_string


def sample_advamced_string_creation():
    '''
    Przykłady zaawansowanego tworzenia ciągu znaków
    '''
    multi_line_string = """To jest wieloliniowy string
    który może być zapisany w wielu liniach
    """
    return multi_line_string


def sample_advamced_string_creation_with_backslash():
    '''
    Przykłady zaawansowanego tworzenia ciągu znaków z użyciem znaku backslash
    '''
    backslash_string = "To jest wieloliniowy string \
    który może być zapisany w wielu liniach"
    return backslash_string


def sample_advamced_string_creation_with_escape_characters():
    '''
    Przykłady zaawansowanego tworzenia ciągu znaków z użyciem znaku backslash i znaków specjalnych (escape characters)
    '''
    raw_string = r"String z użyciem znaku \ (backslash)"
    return raw_string


def sample_advamced_string_creation_with_unicode_characters():
    '''
    Przykłady zaawansowanego tworzenia ciągu znaków z użyciem znaku backslash 
    '''
    unicode_string = r"To jest przykład stringa unicode z polskimi znakami: żółć, ąęśźć"
    return unicode_string


if __name__ == '__main__':
    # Lista funkcji do wykonania
    functions_to_execute = [
        # sample_string_creation,
        # samle_unicode_string_creation
        # samle_unicode_string_creation,
        # sample_advamced_string_creation,
        # sample_advamced_string_creation_with_backslash,
        # sample_advamced_string_creation_with_escape_characters,
        # sample_advamced_string_creation_with_unicode_characters
    ]

    # Wykonanie funkcji z listy oraz wyświetlenie wyników
    for func in functions_to_execute:
        print(func())
