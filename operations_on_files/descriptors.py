# ------------------------ OPERACJE NA PLIKACH ------------------------ #
'''
Natywne moduły Pythona ułatwiające operacje na plikach obejmują:
open() i close(): Wbudowane funkcje umożliwiające otwieranie i zamykanie plików, przy czym deskryptor pliku zwrócony przez open() jest używany do dalszej pracy z plikiem.
os i os.path: Moduły te oferują funkcje do manipulacji strukturą katalogów, sprawdzania istnienia plików, uzyskiwania informacji o plikach, itp.
shutil: Ten moduł dostarcza zaawansowanych funkcji do operacji na plikach i katalogach, takich jak kopiowanie, przenoszenie, usuwanie, archiwizacja, itp.
json: Umożliwia operacje na plikach w formacie JSON, popularnym dla wymiany danych pomiędzy programami.
csv: Umożliwia pracę z plikami CSV (Comma Separated Values), często stosowanymi do przechowywania danych w postaci tabelarycznej.

Komendy w terminalu (Windows):
cd - zmiana katalogu
dir - wyświetlenie zawartości katalogu
mkdir - utworzenie katalogu
rmdir - usunięcie katalogu
del - usunięcie pliku
copy - kopiowanie pliku
move - przeniesienie pliku
ren - zmiana nazwy pliku
. - katalog bieżący
.. - katalog nadrzędny
'''

def sample_txt_file():
    '''
    Otwieramy plik sample.txt, który znajduje się w tym samym katalogu co plik intro.py
    '''
    f = open('sample.txt', 'r')
    print(f.read())
    f.close()


def read_file_operations(file_name='text.txt'):
    '''
    Otwieramy plik text.txt, który znajduje się w tym samym katalogu co plik intro.py
    '''
    with open(file_name, 'r', encoding='utf-8') as file:
        # Odczytanie zawartości pliku
        content = file.read()
        print("Zawartość pliku:", content)

        # Przesunięcie wskaźnika pozycji na początek pliku
        file.seek(0)

        # Odczytanie kolejnych trzech znaków
        partial_content = file.read(3)
        print("Pierwsze trzy znaki:", partial_content)


if __name__ == '__main__':
    # sample_txt_file()
    read_file_operations()