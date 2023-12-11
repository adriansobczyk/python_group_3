# ------------------------ ODCZYT I ZAPIS DO PLIKÓW TXT ------------------------ #

def read_single_line(file_path='sample.txt'):
    '''
    Funkcja odczytuje pierwszą linię z pliku sample.txt, który znajduje się w tym samym katalogu co plik intro.py
    '''
    with open(file_path, 'r') as file:
        line = file.readline()
        print(f"First line: {line.strip()}")


def read_all_lines(file_path='sample.txt'):
    '''
    Funkcja odczytuje wszystkie linie z pliku sample.txt, który znajduje się w tym samym katalogu co plik intro.py
    Użyta jest metoda readlines(), która zwraca listę linii z pliku tekstowego.
    Enumerate() służy do wyliczenia elementów listy oraz indeksu. W tym przypadku wyliczamy linie z pliku tekstowego.
    '''
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            print(f"Line {i}: {line.strip()}")
    # file = open(file_path, 'r')
    # lines = file.readlines()
    # for i, line in enumerate(lines, start=1):
    #     print(f"Line {i}: {line.strip()}")
    # file.close()


def read_line_by_line(file_path='sample.txt'):
    '''
    Funkcja odczytuje plik sample.txt, który znajduje się w tym samym katalogu co plik intro.py
    Użyta jest metoda readline(), która zwraca pojedynczą linię z pliku tekstowego.
    Pętla while odczytuje kolejne linie z pliku tekstowego dopóki nie napotka pustej linii.
    Nie używamy tutaj menadżera kontekstu with open() as file, ponieważ chcemy odczytać kolejne linie z pliku tekstowego.
    '''
    file = open(file_path, 'r')
    line_number = 1
    line = file.readline()
    while line:
        print(f"Line {line_number}: {line.strip()}")
        line = file.readline()
        line_number += 1
    file.close()


if __name__ == '__main__':
    read_single_line()
    read_all_lines()
    read_line_by_line()