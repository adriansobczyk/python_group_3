# ------------------------ METODA CASFOLD ORAZ LOWER ------------------------ #


def compare_str(first, second):
    '''
    Porównanie dwóch ciągów znaków bez względu na wielkość liter (case-insensitive) przy użyciu metody casefold().
    '''
    normalizowany_first = first.casefold()
    normalizowany_second = second.casefold()

    # Porównanie znormalizowanych ciągów
    if normalizowany_first == normalizowany_second:
        print(f"Ciągi '{first}' i '{second}' są identyczne bez względu na wielkość liter.")
    else:
        print(f"Ciągi '{first}' i '{second}' są różne.")


def casefold_vs_lower():
    """
    Porównanie działania metod casefold() i lower() na niemieckim znaku ß.
    """
    ciag = "groß"
    print(f"Metoda casefold(): {ciag.casefold()}")
    print(f"Metoda lower(): {ciag.lower()}")


# if __name__ == "__main__":
    # compare_str("Małe Litery!", "małe liTERY!")
    # casefold_vs_lower()