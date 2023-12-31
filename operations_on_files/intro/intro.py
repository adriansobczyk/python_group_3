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

Komendy w terminalu (Linux):
cd - zmiana katalogu
ls - wyświetlenie zawartości katalogu
mkdir - utworzenie katalogu
rmdir - usunięcie katalogu
rm - usunięcie pliku
cp - kopiowanie pliku
mv - przeniesienie pliku
mv - zmiana nazwy pliku
. - katalog bieżący
.. - katalog nadrzędny

W Pythonie deskryptory plików są obiektami, które reprezentują otwarty plik. Deskryptory plików są używane do interakcji z plikami, zarówno do odczytu, jak i do zapisu danych. 
W Pythonie deskryptory plików są zazwyczaj uzyskiwane przez funkcję open(), która otwiera plik i zwraca obiekt deskryptora pliku.
Podstawowe operacje, które można wykonywać za pomocą deskryptorów plików w Pythonie, 
to czytanie (read()), pisanie (write()), przesuwanie wskaźnika pozycji (seek()), zamykanie pliku (close()), sprawdzanie pozycji wskaźnika (tell()), itp.
'''

def sample_txt_file():
    '''
    Otwieramy plik sample.txt, który znajduje się w tym samym katalogu co plik intro.py
    '''
    f = open(r'intro/sample.txt') # nazwa folderu i pliku, r - raw string (nie interpretuje znaków specjalnych)
    print(f.read())
    f.close()


def read_file_operations(file_name=r'intro/sample.txt'):
    '''
    Otwieramy plik text.txt, który znajduje się w tym samym katalogu co plik intro.py
    '''
    with open(file_name, 'r', encoding='utf-8') as f:
        # Odczytanie zawartości pliku
        content = f.read()
        print("Zawartość pliku:", content)

        # Przesunięcie wskaźnika pozycji na początek pliku
        f.seek(0)

        # Odczytanie kolejnych trzech znaków
        partial_content = f.read(2)
        print("Pierwsze trzy znaki:", partial_content)