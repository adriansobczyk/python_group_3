# ---------------------- Funkcje ---------------------- #

def mnozy_razy_dwa(liczba):
    # Tutaj umieść logikę pierwszej funkcji, która operuje na liczbie
    wynik = liczba * 2
    print(f"Wynik mnożenia liczby {liczba} razy 2 to {wynik}")
    return wynik

def druga_funkcja(liczba):
    # Wywołaj pierwszą funkcję i przypisz jej wynik do zmiennej
    output_pierwszej_funkcji = mnozy_razy_dwa(liczba)
    output_pierwszej_funkcji += 10
    
    # Tutaj możesz użyć wyniku pierwszej funkcji
    wynik_drugiej_funkcji = f"Output z pierwszej funkcji: {output_pierwszej_funkcji}"
    return wynik_drugiej_funkcji

# Przykład użycia: przekazujemy liczbę 5 do obu funkcji
print(druga_funkcja(5))


# ---------------------- Funkcje zagnieżdżone ---------------------- #
# Przykład 1: Zagnieżdżona funkcja zwracająca kwadrat liczby

def oblicz_kwadrat(x):
    # Zagnieżdżona funkcja do obliczenia potęgi
    def potega(y):
        return y ** 2
    def szescian(y):
        return y ** 3
    def suma(y):
        return y + y
    
    # Wywołanie zagnieżdżonej funkcji
    wynik_potega = potega(x)
    wynik_szescian = szescian(x)
    wynik_suma = suma(x)
    return wynik_suma


# Wywołanie głównej funkcji
liczba = 5
wynik_kwadratu = oblicz_kwadrat(liczba)
wynik_suma = oblicz_kwadrat(liczba)
print(f"Kwadrat liczby {liczba} to {wynik_kwadratu}")
print(f"Suma liczby {liczba} to {wynik_suma}")


# Przykład 2: Zagnieżdżona funkcja obsługująca listy

def przetworz_liste(lista):
    # Zagnieżdżona funkcja do podwojenia elementów listy
    def podwoj_elementy():
        return [element * 2 for element in lista]
    
    # Wywołanie zagnieżdżonej funkcji
    przetworzona_lista = podwoj_elementy()
    return przetworzona_lista

# Wywołanie głównej funkcji
# moja_lista = [1, 2, 3, 4]
# wynik_przetworzenia = przetworz_liste(moja_lista)
# print(f"Przetworzona lista: {wynik_przetworzenia}")

# ---------------------- Zmienne lokalne ---------------------- #
def funkcja():
    local_variable = 5
    print(local_variable)

# funkcja()

# ---------------------- Zmienne globalne ---------------------- #

def zewnetrzna_funkcja():
    '''
    Słowo kluczowe nonlocal jest używane wewnątrz zagnieżdżonych funkcji i wskazuje, 
    że zmienna powinna być szukana w zakresie powyżej bieżącej funkcji, ale nie w najwyższym zakresie (globalnym).
    '''
    outer_variable = 10
    def wewnetrzna_funkcja():
        nonlocal outer_variable
        outer_variable = 20
        print(outer_variable)
    wewnetrzna_funkcja()

# zewnetrzna_funkcja()







def zewnetrzna_funkcja():
    outer_variable = 10
    print("Przed wewnetrzna_funkcja:", outer_variable)

    def wewnetrzna_funkcja():
        nonlocal outer_variable
        outer_variable = 20
        print("Wewnątrz wewnetrzna_funkcja:", outer_variable)

    wewnetrzna_funkcja()  # Wywołanie wewnetrzna_funkcja zmienia wartość outer_variable
    print("Po wewnetrzna_funkcja:", outer_variable)

# zewnetrzna_funkcja()


# ---------------------- Zmienne globalne ---------------------- #

global_variable = 10

def funkcja():
    '''
    Słowo kluczowe global jest używane do wskazania, 
    że zmienna powinna być szukana w najwyższym zakresie, czyli w zakresie globalnym.
    '''
    global global_variable
    global_variable = 20
    # print(global_variable)

# funkcja()
# print(global_variable)
