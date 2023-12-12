# ------------------------ MENADŻER KONTEKSTU ------------------------ #

def read_file_with_open(sciezka=r'context_manager/sample_user_data.txt'):
    with open(sciezka, 'r', encoding='utf-8') as plik:
        zawartosc = plik.readlines()
        print(zawartosc)
    # Plik zostanie automatycznie zamknięty po zakończeniu bloku with


def czytaj_plik_open(sciezka=r'context_manager/sample_user_data.txt'):
    plik = open(sciezka, 'r', encoding='utf-8')
    try:
        zawartosc = plik.readlines()
        print(zawartosc)
    finally:
        plik.close()
    # Plik zostanie zamknięty po zakończeniu bloku try-finally


if __name__ == '__main__':
    read_file_with_open()
    czytaj_plik_open()