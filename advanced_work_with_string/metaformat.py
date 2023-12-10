# ------------------------ METAJĘZYK FORMATOWANIA ------------------------ #

def meta_format_modificators():
    # Definiowanie innych zmiennych
    first_name = "Adrian"
    surname = "Johnson"
    # print(type(first_name))

    # Użycie mini-języka formatowania ciągów znaków
    s = "{first_name} {surname}".format(surname=surname, first_name=first_name)
    print("Bez modyfikatorów:", s)

    # # Użycie modyfikatora !r
    s = "{first_name!r} {surname}".format(surname=surname, first_name=first_name)
    print("Z modyfikatorem !r:", s)

    # # Użycie modyfikatora !r
    s = "{first_name} {surname!r}".format(surname=surname, first_name=first_name)
    print("Z modyfikatorem !r:", s)

    # # Użycie modyfikatora !s
    s = "{first_name} {surname!s}".format(surname=surname, first_name=first_name)
    print("Z modyfikatorem !s:", s)


from datetime import datetime
def meta_format_modificators_multiple_data_types():
    current_date = datetime.now()
    liczba = 42
    tekst = "Przykładowy tekst"
    lista = [1, 2, 3, 4, 5]

    # Użycie mini-języka formatowania ciągów znaków z różnymi modyfikatorami
    formatted_text = "Data: {data}, Liczba: {liczba}, Tekst: {tekst}, Lista: {lista}".format(
        data=current_date,
        liczba=liczba,
        tekst=tekst,
        lista=lista
    )

    print("Bez modyfikatorów:", formatted_text)

    formatted_text_repr = "Data: {data!r}, Liczba: {liczba!r}, Tekst: {tekst!r}, Lista: {lista!r}".format(
        data=current_date,
        liczba=liczba,
        tekst=tekst,
        lista=lista
    )

    print("Z modyfikatorem !r:", formatted_text_repr)

    formatted_text_str = "Data: {data}, Liczba: {liczba!s}, Tekst: {tekst}, Lista: {lista}".format(
        data=current_date,
        liczba=liczba,
        tekst=tekst,
        lista=lista
    )

    print("Z modyfikatorem !s:", formatted_text_str)


def meta_format_decimal_representation():
    '''
    Funkcja prezentuje sposoby formatowania liczb całkowitych.
    '''
    print('{:^10} {:^10} {:^10}'.format('liczba', 'kwadrat', 'sześcian'))
    print('{:^10} {:^10} {:^10}'.format('-------', '-------', '-------'))
    for num in range(12):
        print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))


def meta_format_hex_representation():
    '''
    Funkcja prezentuje sposoby formatowania liczb całkowitych.
    '''
    print('{:^10} {:^10} {:^10}'.format('liczba', 'kwadrat', 'sześcian'))
    print('{:^10} {:^10} {:^10}'.format('-------', '-------', '-------'))
    for num in range(12):
        print('{:^10} {:^10} {:^10}'.format(hex(num), hex(num**2), hex(num**3)))


def meta_format_oct_representation():
    '''
    Funkcja prezentuje sposoby formatowania liczb całkowitych.
    '''
    print('{:^10} {:^10} {:^10}'.format('liczba', 'kwadrat', 'sześcian'))
    print('{:^10} {:^10} {:^10}'.format('-------', '-------', '-------'))
    for num in range(12):
        print('{:^10} {:^10} {:^10}'.format(oct(num), oct(num**2), oct(num**3)))
    

def meta_format_bin_representation():
    '''
    Funkcja prezentuje sposoby formatowania liczb całkowitych.
    '''
    print('{:^10} {:^10} {:^10}'.format('liczba', 'kwadrat', 'sześcian'))
    print('{:^10} {:^10} {:^10}'.format('-------', '-------', '-------'))
    for num in range(12):
        print('{:^10} {:^10} {:^10}'.format(bin(num), bin(num**2), bin(num**3)))


def decimal_to_binary(decimal_number):
    binary_representation = "{0:#b}".format(decimal_number)
    hex_representation = "{0:#x}".format(decimal_number)
    oct_representation = "{0:#o}".format(decimal_number)
    return binary_representation, hex_representation, oct_representation


def binary_to_decimal(binary_string):
    decimal_number = int(binary_string, 2)
    return decimal_number


# if __name__ == '__main__':
    # meta_format_modificators()
    # meta_format_modificators_multiple_data_types()
    # meta_format_decimal_representation()
    # meta_format_hex_representation()
    # meta_format_oct_representation()
    # meta_format_bin_representation()

    # for i in range(1, 16):
    #     decimal = i
    #     binary = decimal_to_binary(decimal)
    #     print(f"Decimal: {decimal}, Binary: {binary}, Hex: {hex(decimal)}, Oct: {oct(decimal)}")

    # binary_data = "1101"
    # decimal_result = binary_to_decimal(binary_data)
    # print(f"Binary: {binary_data}, Decimal: {decimal_result}")