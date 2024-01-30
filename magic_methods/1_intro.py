'''
1. Wprowadzenie do metod magicznych
'''

# Metody magiczne to metody, które zaczynają się i kończą podwójnym podkreśleniem.
# Są to metody, które mają specjalne znaczenie dla Pythona.
# Nie powinno się tworzyć metod magicznych w swoich klasach, ponieważ mogą one
# nadpisywać istniejące metody magiczne i w ten sposób zmieniać ich działanie.

# Lista metod magicznych:

# __init__ - metoda wywoływana podczas tworzenia nowego obiektu
# __str__ - metoda wywoływana podczas konwersji obiektu na napis

# __add__ - metoda wywoływana podczas dodawania dwóch obiektów +
# __sub__ - metoda wywoływana podczas odejmowania dwóch obiektów -
# __mul__ - metoda wywoływana podczas mnożenia dwóch obiektów *
# __truediv__ - metoda wywoływana podczas dzielenia dwóch obiektów /
# __floordiv__ - metoda wywoływana podczas dzielenia całkowitoliczbowego dwóch obiektów
# __mod__ - metoda wywoływana podczas dzielenia modulo dwóch obiektów %
# __pow__ - metoda wywoływana podczas potęgowania dwóch obiektów **

# __eq__ - metoda wywoływana podczas porównywania dwóch obiektów za pomocą operatora ==
# __ne__ - metoda wywoływana podczas porównywania dwóch obiektów za pomocą operatora !=
# __lt__ - metoda wywoływana podczas porównywania dwóch obiektów za pomocą operatora <
# __gt__ - metoda wywoływana podczas porównywania dwóch obiektów za pomocą operatora >

# __len__ - metoda wywoływana podczas wywołania funkcji len() na obiekcie
# __getitem__ - metoda wywoływana podczas pobierania elementu z obiektu za pomocą operatora []
# __setitem__ - metoda wywoływana podczas ustawiania elementu w obiekcie za pomocą operatora []
# __delitem__ - metoda wywoływana podczas usuwania elementu z obiektu za pomocą operatora []
# __contains__ - metoda wywoływana podczas sprawdzania czy obiekt zawiera dany element za pomocą operatora in

# __enter__ - metoda wywoływana podczas wejścia do bloku with
# __exit__ - metoda wywoływana podczas wyjścia z bloku with

# __call__ - metoda wywoływana podczas wywołania obiektu jak funkcji
# __del__ - metoda wywoływana podczas usuwania obiektu

# __new__ - metoda wywoływana podczas tworzenia nowego obiektu
# __class__ - atrybut przechowujący klasę obiektu
# __dict__ - atrybut przechowujący słownik z atrybutami obiektu
# __doc__ - atrybut przechowujący dokumentację obiektu
# __name__ - atrybut przechowujący nazwę obiektu
# __module__ - atrybut przechowujący nazwę modułu, w którym znajduje się obiekt
# __bases__ - atrybut przechowujący krotkę z klasami bazowymi obiektu

# __slots__ - atrybut przechowujący krotkę z nazwami atrybutów, które mogą być przechowywane w obiekcie
# __weakref__ - atrybut przechowujący słownik z obiektami, które referencjonują obiekt

# __format__ - metoda wywoływana podczas formatowania obiektu za pomocą funkcji format()
# __hash__ - metoda wywoływana podczas wywołania funkcji hash() na obiekcie

# __index__ - metoda wywoływana podczas konwersji obiektu na liczbę całkowitą
# __int__ - metoda wywoływana podczas konwersji obiektu na liczbę całkowitą
# __float__ - metoda wywoływana podczas konwersji obiektu na liczbę zmiennoprzecinkową
# __bool__ - metoda wywoływana podczas konwersji obiektu na wartość logiczną

# __iter__ - metoda wywoływana podczas iterowania po obiekcie
# __next__ - metoda wywoływana podczas pobierania kolejnego elementu iteracji

# __reversed__ - metoda wywoływana podczas odwracania obiektu
# __abs__ - metoda wywoływana podczas obliczania wartości bezwzględnej obiektu
# __round__ - metoda wywoływana podczas zaokrąglania obiektu
# __ceil__ - metoda wywoływana podczas zaokrąglania obiektu w górę
# __floor__ - metoda wywoływana podczas zaokrąglania obiektu w dół