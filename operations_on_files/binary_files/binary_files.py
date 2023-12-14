# ------------------------ PLIKI BINARNE ------------------------ #

def create_binary_file():
    with open('binary_files/binary_file.bin', 'wb') as file:
        file.write(b'Hello World!')

def read_binary_file():
    with open('binary_files/binary_file.bin', 'rb') as file:
        print(file.read())

def read_binary_file_with_encoding():
    with open('binary_files/binary_file.bin', 'rb') as file:
        print(file.read().decode('utf-8'))

def append_binary_file():
    with open('binary_files/binary_file.bin', 'ab') as file:
        file.write(b'Hello World!\n')


def zapisz_do_pliku_binarnego(nazwa_pliku="binary_files/plik_binarny.bin", dane=b'Hello, World!'):
    try:
        with open(nazwa_pliku, 'wb') as plik:
            # Zapis danych do pliku binarnego
            plik.write(dane)
        print(f'Dane zostały zapisane do pliku binarnego "{nazwa_pliku}".')
    except IOError as e:
        print(f'Błąd podczas zapisu do pliku: {e}')

# if __name__ == '__main__':
    # create_binary_file()
    # read_binary_file()
    # read_binary_file_with_encoding()
    # append_binary_file()
    # zapisz_do_pliku_binarnego()