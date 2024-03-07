# ------------------------ KODOWANIE CIĄGÓW (ASCII, UTF-8, CP1251) ------------------------ #

def sample_ord():
    """
    Funkcja zwraca wartość liczbową znaku ASCII.
    """
    char = "a"
    print(ord(char))


def sample_chr():
    """
    Funkcja zwraca znak ASCII dla podanej wartości liczbowej.
    """
    number = 97
    print(chr(number))

def ascii_with_polish_letters():
    """
    Funkcja koduje polskie znaki diakrytyczne do ASCII.
    """
    string = "Cześć!"
    string = string.encode("ascii", "ignore")
    print(string)

def utf8_with_polish_letters():
    """
    Funkcja koduje polskie znaki diakrytyczne do UTF-8.
    """
    string = "Cześć!"
    string = string.encode("utf-8")
    print(string)

def utf16_with_polish_letters():
    """
    Funkcja koduje polskie znaki diakrytyczne do UTF-16.
    """
    string = "Cześć!"
    string = string.encode("utf-16")
    print(string)

def utf32_with_polish_letters():
    """
    Funkcja koduje polskie znaki diakrytyczne do UTF-32.
    """
    string = "Cześć!"
    string = string.encode("utf-32")
    print(string)

def decode_ascii():
    """
    Funkcja dekoduje ciąg znaków ASCII.
    """
    string = b"Czesc!"
    string = string.decode("ascii")
    print(string)


def decodeascii_with_polish_letters():
    """
    Funkcja dekoduje ciąg znaków ASCII z polskimi znakami diakrytycznymi.
    """
    # Mapowanie polskich liter na odpowiedniki angielskie
    polish_to_english = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    string = "Cześć!"
    # Zamienia polskie litery na odpowiedniki angielskie
    for polish, english in polish_to_english.items():
        string = string.replace(polish, english)
    
    # Koduje ciąg znaków do ASCII
    string = string.encode("ascii", "ignore")
    print(string)

def decode_utf8():
    """
    Funkcja dekoduje ciąg znaków UTF-8.
    """
    string = b"Cze\xc5\x9b\xc4\x87!"
    string = string.decode("utf-8")
    print(string)

def decode_utf16():
    """
    Funkcja dekoduje ciąg znaków UTF-16.
    """
    string = b"\xff\xfeC\x00z\x00e\x00s\x00c\x00!\x00"
    string = string.decode("utf-16")
    print(string)

# if __name__ == '__main__':
    # ascii_with_polish_letters()
    # utf8_with_polish_letters()
    # utf16_with_polish_letters()
    # utf32_with_polish_letters()
    # decode_ascii()
    # decodeascii_with_polish_letters()
    # decode_utf8()
    # decode_utf16()