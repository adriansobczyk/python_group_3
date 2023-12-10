# ------------------------ ZNAKI SPECJALNE ------------------------ #

# Przykład 1 - znak \n - nowa linia
def sample_new_line():
    '''
    Przykład użycia znaku \n
    '''
    string_with_new_line = "To jest przykład stringa z nową linią.\nTo jest druga linia."
    return string_with_new_line


# Przykład 2 - znak \f - nowa strona
def sample_new_page():
    '''
    Przykład użycia znaku \f
    '''
    string_with_new_page = "To jest przykład\fstringa z nową stroną"
    return string_with_new_page


# Przykład 3 - znak \r - powrót karetki (przesunięcie kursora na początek linii)
def sample_carriage_return():
    '''
    Przykład użycia znaku \r
    '''
    string_with_carriage_return = "To jest przykład\rstringa z powrotem karetki"
    return string_with_carriage_return


# Przykład 4 - znak \t - tabulator
def sample_tab():
    '''
    Przykład użycia znaku \t
    '''
    string_with_tab = "To jest przykład\tstringa z tabulatorem"
    return string_with_tab


# Przykład 5 - znak \b - backspace
def sample_backspace():
    '''
    Przykład użycia znaku \b
    '''
    string_with_backspace = "To jest przykład\bstringa z backspace"
    return string_with_backspace


# Przykład 6 - znak \v - pionowa tabulacja
def sample_vertical_tab():
    '''
    Przykład użycia znaku \v
    '''
    string_with_vertical_tab = "To jest przykład\vstringa z pionową tabulacją"
    return string_with_vertical_tab


def save_functions_output_to_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(sample_new_line() + '\n')
        file.write(sample_new_page() + '\n')
        file.write(sample_carriage_return() + '\n')
        file.write(sample_tab() + '\n')
        file.write(sample_backspace() + '\n')
        file.write(sample_vertical_tab() + '\n')


# if __name__ == '__main__':
    # print(sample_new_line())
    # print(sample_new_page())
    # print(sample_carriage_return())
    # print(sample_tab())
    # print(sample_backspace())
    # print(sample_vertical_tab())
    # filename = 'output.txt'
    # save_functions_output_to_file(filename)