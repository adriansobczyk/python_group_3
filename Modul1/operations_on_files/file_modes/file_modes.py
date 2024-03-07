# ------------------------ TRYBY OTWIERANIA PLIKÓW ------------------------ #
'''
r - read (czytanie) - domyślny tryb, otwiera plik do odczytu, jeśli plik nie istnieje to zwraca błąd
w - write (pisanie) - otwiera plik do zapisu, jeśli plik nie istnieje to go tworzy, jeśli istnieje to go kasuje
a - append (dopisywanie) - otwiera plik do dopisywania, jeśli plik nie istnieje to go tworzy
r+ - read and write (czytanie i pisanie) - otwiera plik do odczytu i zapisu, jeśli plik nie istnieje to zwraca błąd
w+ - write and read (pisanie i czytanie) - otwiera plik do zapisu i odczytu, jeśli plik nie istnieje to go tworzy, jeśli istnieje to go kasuje
a+ - append and read (dopisywanie i czytanie) - otwiera plik do dopisywania i odczytu, jeśli plik nie istnieje to go tworzy
x - exclusive creation (ekskluzywne tworzenie) - otwiera plik do zapisu, jeśli plik nie istnieje to go tworzy, jeśli istnieje to zwraca błąd
'''

def sample_read_file():
    '''
    Funkcja otwiera plik sample.txt.
    '''
    f = open(r'file_modes/sample.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


def sample_write_file():
    '''
    Funkcja otwiera oraz zapisuje do pliku sample.txt oraz zwraca liczbę zapisanych znaków (w tym przypadku 18).
    '''
    # Bez używania menadżera kontekstu
    # f = open('file_modes/sample.txt', 'w')
    # f.write('Hello World! Write')
    # f.close()

    # Z menadżerem kontekstu - with
    with open(r'file_modes/sample.txt', 'w', encoding='utf-8') as f:
        print(f.write('Hello World! Write'))


def sample_append_file():
    '''
    Funckcja otwiera oraz dopisuje do pliku sample.txt oraz dodaje nową linię.
    '''
    f = open(r'file_modes/sample.txt', 'a')
    f.write('\nHello World! Append')
    f.close()


def sample_read_write_file():
    '''
    Funkcja otwiera plik sample.txt oraz zapisuje do niego linię tekstu.
    '''
    f = open(r'file_modes/sample.txt', 'r+')
    print(f.read())
    f.write('\nHello World! Read Write')
    f.close()


def sample_write_read_file():
    '''
    Otwieramy plik sample.txtJeśli plik nie istnieje to go utworzy. Jeśli istnieje to go skasuje.
    '''
    f = open(r'file_modes/sample.txt', 'w+')
    f.write('Hello World! Write Read')
    print(f.read())
    f.close()


def sample_append_read_file():
    '''
    Funkcja otwiera plik sample.txt Jeśli plik nie istnieje to go utworzy.
    '''
    f = open(r'file_modes/sample.txt', 'a+')
    f.write('\nHello World! Append Read')
    print(f.read())
    f.close()


def sample_exclusive_creation_file():
    '''
    Funkcja otwiera plik sample.txt. Jeśli plik nie istnieje to go utworzy. Jeśli istnieje to zwróci błąd.
    '''
    f = open(r'file_modes/sample_two.txt', 'x')
    f.write('Hello World! Exclusive Creation')
    f.close()


if __name__ == '__main__':
    # sample_read_file()
    sample_write_file()
    # sample_append_file()
    # sample_read_write_file()
    # sample_write_read_file()
    # sample_append_read_file()
    # sample_exclusive_creation_file()