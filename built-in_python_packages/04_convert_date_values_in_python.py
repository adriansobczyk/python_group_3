'''
Konwertowanie na ciąg i odwrotnie
'''

from datetime import datetime

def convert_date_to_string(data_godzina, format='%Y-%m-%d %H:%M:%S'):
    """
    Konwertuje obiekt daty/godziny na ciąg znaków. Więcej informacji na temat formatów daty i godziny:
    https://www.w3schools.com/python/python_datetime.asp

    Args:
    - data_godzina (datetime): Obiekt daty/godziny do skonwertowania.
    - format (str): Format ciągu znaków do użycia. Domyślnie '%Y-%m-%d %H:%M:%S'.

    Returns:
    - str: Skonwertowany ciąg znaków.
    """
    return data_godzina.strftime(format)


def convert_string_to_date(ciag_znakow, format='%Y-%m-%d %H:%M:%S'):
    """
    Konwertuje ciąg znaków na obiekt daty/godziny.

    Args:
    - ciag_znakow (str): Ciąg znaków do skonwertowania.
    - format (str): Format ciągu znaków. Domyślnie '%Y-%m-%d %H:%M:%S'.

    Returns:
    - datetime: Obiekt daty/godziny.
    """
    return datetime.strptime(ciag_znakow, format)


def convert_and_change_format(data, obecny_format='%Y-%m-%d %H:%M:%S', nowy_format='%B %d, %Y, %I:%M:%S %p'):
    """
    Konwertuje datę na ciąg znaków i zmienia jej format.

    Args:
    - data (datetime): Obiekt daty do konwersji.
    - obecny_format (str): Obecny format daty. Domyślnie '%Y-%m-%d %H:%M:%S'.
    - nowy_format (str): Nowy format daty. Domyślnie '%m-%d-%Y %H:%M:%S'.

    Returns:
    - str: Skonwertowany ciąg znaków w nowym formacie.
    """
    # Konwersja daty do ciągu znaków w obecnym formacie
    data_jako_str = data.strftime(obecny_format)

    # Konwersja ciągu znaków do daty w obecnym formacie
    data_obiekt = datetime.strptime(data_jako_str, obecny_format)

    # Konwersja daty do ciągu znaków w nowym formacie
    data_w_nowym_formacie = data_obiekt.strftime(nowy_format)

    return data_w_nowym_formacie


if __name__ == "__main__":
    # Przykład konwersji daty na ciąg znaków
    data = datetime(year=2024, month=1, day=2, hour=20, minute=0, second=0)
    data_jako_str = convert_date_to_string(data)
    print(f"Data jako ciąg znaków: {data_jako_str}")
    # Przykład konwersji ciągu znaków na datę
    data_jako_str = "2024-01-02 20:00:00"
    data = convert_string_to_date(data_jako_str)
    print(f"Data jako obiekt daty: {data}")
    # Przykład konwersji daty na ciąg znaków i zmiany formatu
    data = datetime(year=2024, month=1, day=2, hour=20, minute=0, second=0)
    data_w_nowym_formacie = convert_and_change_format(data)
    print(f"Data w nowym formacie: {data_w_nowym_formacie}")