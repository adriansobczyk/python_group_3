# ------------------------ CIĄGI BAJTÓW, TABLICE BAJTÓW ------------------------ #


def convert_str_to_bytes():
    """
    Funkcja konwertuje ciąg znaków na ciąg bajtów.
    """
    string = "Hi user!"
    bytes_string = bytes(string, encoding="utf-8")
    print(bytes_string)


def convert_bytes_to_str():
    """
    Funkcja konwertuje ciąg bajtów na ciąg znaków.
    """
    bytes_string = b"Hi user!"
    string = str(bytes_string, encoding="utf-8")
    print(string)


def convert_str_to_bytesarray():
    """
    Funkcja konwertuje ciąg znaków na tablicę bajtów.
    """
    string = "Hi user!"
    bytes_array = bytearray(string, encoding="utf-8")
    print(bytes_array)


def convert_bytesarray_to_str():
    """
    Funkcja konwertuje tablicę bajtów na ciąg znaków.
    """
    bytes_array = bytearray(b"Hi user!")
    string = str(bytes_array, encoding="utf-8")
    print(string)


def convert_bytes_to_bytesarray():
    """
    Funkcja konwertuje ciąg bajtów na tablicę bajtów.
    """
    bytes_string = b"Hi user!"
    bytes_array = bytearray(bytes_string)
    print(bytes_array)


def convert_bytesarray_to_bytes():
    """
    Funkcja konwertuje tablicę bajtów na ciąg bajtów.
    """
    bytes_array = bytearray(b"Hi user!")
    bytes_string = bytes(bytes_array)
    print(bytes_string)


def convert_int_to_bytes():
    """
    Funkcja konwertuje liczbę całkowitą na ciąg bajtów.
    """
    number = 10
    bytes_number = bytes(number)
    print(bytes_number)


def convert_list_to_bytesarray():
    """
    Funkcja konwertuje listę na tablicę bajtów.
    """
    list = [1, 2, 3, 4, 5]
    bytes_array = bytearray(list)
    print(bytes_array)


def convert_dict_to_bytesarray():
    """
    Funkcja konwertuje słownik na tablicę bajtów.
    """
    my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 10}
    print(my_dict)
    convert_bytes_to_bytesarray= str(my_dict).encode("utf-8")
    bytes_array = bytearray(convert_bytes_to_bytesarray)
    print(bytes_array)


def convert_to_hex():
    """
    Funkcja konwertuje ciąg bajtów na ciąg znaków zapisany w systemie szesnastkowym.
    """
    bytes_string = "Hi user!".encode("utf-8")
    hex_string = bytes_string.hex()
    print(hex_string)
    some_numbers = bytes([1, 2, 3, 4, 5])
    print(some_numbers)
    for number in some_numbers:
        print(hex(number))

def convert_hex_to_bytes():
    """
    Funkcja konwertuje ciąg znaków zapisany w systemie szesnastkowym na ciąg bajtów.
    """
    hex_string = "4869207573657221"
    bytes_string = bytes.fromhex(hex_string)
    print(bytes_string)

# if __name__ == "__main__":
    # convert_str_to_bytes()
    # convert_bytes_to_str()
    # convert_str_to_bytesarray()
    # convert_bytesarray_to_str()
    # convert_bytes_to_bytesarray()
    # convert_bytesarray_to_bytes()
    # convert_int_to_bytes()
    # convert_list_to_bytesarray()
    # convert_dict_to_bytesarray()
    # convert_to_hex()
    # convert_hex_to_bytes()