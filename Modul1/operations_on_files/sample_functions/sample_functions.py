# ------------------------ PRZYKŁADOWE FUNKCJE ------------------------ #
import re


def create_txt_with_int_and_calculate_sum(file_path=r'sample_functions/numbers.txt'):
    '''
    Funkcja tworzy plik numbers.txt, który znajduje się w tym samym katalogu co plik intro.py
    Następnie zapisuje do niego liczby całkowite od 1 do 100.
    Na koniec odczytuje plik numbers.txt i sumuje wszystkie liczby całkowite.
    '''
    with open(file_path, 'w') as file:
        for i in range(1, 101):
            file.write(f"{i}\n")
    with open(file_path, 'r') as file:
        numbers = file.readline()
        sum = 0
        while numbers:
            sum += int(numbers)
            numbers = file.readline()
    print(f"Sum: {sum}")


def create_file_with_info(file_path=r'sample_functions/sample_user_data.txt', name='Jan', surname='Kowalski', nickname='jkowalski'):
    '''
    Funkcja tworzy plik sample_user_data.txt, który znajduje się w tym samym katalogu co plik intro.py
    Następnie zapisuje do niego informacje o użytkowniku.
    '''
    try:
        file = open(file_path, 'w', encoding='utf-8')
        file.write(f"Imię: {name}\n")
        file.write(f"Nazwisko: {surname}\n")
        file.write(f"Nickname: {nickname}\n")
        print(f"Plik {file_path} został utworzony z informacjami.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        if file:
            file.close()


def read_file_to_list(file_path=r'sample_functions/sample_user_data.txt'):
    result = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    result.append(line.strip())
            else:
                print("Pusty plik.")
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytu pliku: {e}")

    return result


def read_file_to_dict(file_path=r'sample_functions/sample_user_data.txt'):
    '''
    Funkcja odczytuje plik i zwraca słownik z danymi użytkownika.
    '''
    result_dict = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    key, value = map(str.strip, line.split(':'))
                    result_dict[key] = value
            else:
                print("Pusty plik.")
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytu pliku: {e}")
    return result_dict

def read_keys_from_file(file_path=r'sample_functions/sample_user_data.txt'):
    keys_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                key, _ = line.strip().split(':')
                keys_list.append(key.strip())
        return keys_list
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytywania pliku: {e}")
        return None


def read_values_from_file(file_path=r'sample_functions/sample_user_data.txt'):
    '''
    Funkcja odczytuje plik i zwraca listę wartości.
    '''
    values_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                _, value = line.strip().split(':')
                values_list.append(value.strip())
        return values_list
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytywania pliku: {e}")
        return None


def extract_sentences():
    '''
    Funkcja wyszukuje wszystkie zdania zawierające słowo "Python" lub "python" w pliku python.txt.
    Następnie wydrukuje wyniki.
    '''
    with open(r'sample_functions/python_text.txt', 'r') as file:
        text = file.read()
    # Wyrażenie regularne do wyszukiwania wszystkich zdań zawierających "Python" lub "python"
    sentences_pattern = re.compile(r'[^.]*\bPython\b[^.]*\.|[^.]*\bpython\b[^.]*\.')
    # Wyszukiwanie i wydruk wyniku
    matches = sentences_pattern.findall(text)
    if matches:
        print("Wydobyte zdania:")
        for match in matches:
            print(match)
    else:
        print("Nie znaleziono pasujących zdań.")


def find_words_in_file_in_text():
    '''
    Funkcja wyszukuje ilości wystąpień słów z listy w tekście.
    Następnie wydrukuje wyniki.
    '''
    # Pobieranie ścieżki do pliku z listą słów od użytkownika
    words_file_path = input("Podaj ścieżkę do pliku z listą słów: ") # sample_functions/sample_list_of_words.txt

    # Otwieranie pliku z listą słów
    with open(words_file_path, 'r') as words_file:
        # Odczyt słów do listy
        words_list = words_file.read().split()

    # Pobieranie ścieżki do pliku z tekstem od użytkownika
    text_file_path = input("Podaj ścieżkę do pliku z tekstem: ") # sample_functions/sample_text_file.txt

    # Otwieranie pliku z tekstem
    with open(text_file_path, 'r') as text_file:
        # Odczyt całego tekstu
        text = text_file.read()

    # Inicjowanie słownika do przechowywania informacji o ilości wystąpień każdego słowa
    word_count = {word: 0 for word in words_list}

    # Iterowanie przez każde słowo na liście
    for word in words_list:
        # Wyszukiwanie ilości wystąpień każdego słowa w tekście (ignorowanie wielkości liter)
        occurrences = text.lower().count(word.lower())
        # Dodawanie wyników do słownika
        word_count[word] = occurrences

    # Wydruk wyników
    for word, count in word_count.items():
        print(f"Słowo '{word}' występuje {count} razy.")


def sample_function_with_two_files(sample_file_source=r'sample_functions/sample_text_file.txt', sample_file_ouput=r'sample_functions/sample_text_file_copy.txt'):
    '''
    Funkcja odczytuje plik źródłowy i zapisuje do pliku wyjściowego
    '''
    try:
        with open(sample_file_source, 'r') as source_file:
            with open(sample_file_ouput, 'w') as output_file:
                for line in source_file:
                    output_file.write(line)
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


# if __name__ == '__main__':
    # create_txt_with_int_and_calculate_sum()
    # create_file_with_info()
    # print(read_file_to_list())
    # print(read_file_to_dict())
    # print(read_keys_from_file())
    # print(read_values_from_file())
    # extract_sentences()
    # find_words_in_file_in_text()
    # sample_function_with_two_files()