from modul_os.modul_os import get_current_directory
from intro.intro import sample_txt_file
from context_manager.context_manager import read_file_with_open

'''
Z blokiem if __name__ == "__main__":
Gdy plik main.py jest uruchamiany bezpośrednio (nie jest importowany jako moduł), kod wewnątrz bloku if __name__ == "__main__": zostanie wykonany.
Jeśli plik jest importowany jako moduł w innym skrypcie, kod wewnątrz tego bloku nie zostanie wykonany automatycznie.

Bez bloku if __name__ == "__main__"::
Kod zostanie wykonany zaraz po imporcie pliku, bez względu na to, czy jest uruchamiany bezpośrednio czy importowany jako moduł.
To podejście może prowadzić do przypadkowego wykonania kodu, który nie jest przeznaczony do bezpośredniego uruchamiania, gdy plik jest importowany jako moduł.
'''

if __name__ == "__main__":
    sample_txt_file()
    read_file_with_open()