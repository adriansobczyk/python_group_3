'''
8. Wyjątki w Pythonie
'''

from datetime import datetime
# from pytz import timezone  # Do obsługi stref czasowych

# Przykład 1
def sample_add_function(a, b):
    try:
        print(a + b)
    except Exception:
        print("Nie można dodać tych dwóch liczb")
    # finally:
    #     print("Koniec działania funkcji")

# sample_add_function(1, 'abc')


# Przykład 2 - pisanie własnych wyjątków
class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Mój niestandardowy wyjątek: {self.message}"

# def sample_add_function(a, b):
#     if not isinstance(a, int) or not isinstance(b, int):
#         raise MyException("Nie można dodać tych dwóch liczb")
#     print(a + b)

def test_function(a, b):
    try:
        sample_add_function(a, b)
    except MyException as e:
        print(e)

# test_function(1, 'abc')


# Przykład 3
class BladMatematyczny(Exception):
    """Klasa bazowa dla błędów matematycznych."""
    def __init__(self, message="Wystąpił błąd matematyczny."):
        self.message = message
        super().__init__(self.message)

class BladDodawania(BladMatematyczny):
    def __init__(self, a, b):
        message = f"Błąd podczas dodawania {a} i {b}. Nie można dodawać tych wartości."
        super().__init__(message)

class BladOdejmowania(BladMatematyczny):
    def __init__(self, a, b):
        message = f"Błąd podczas odejmowania {b} od {a}. Nie można odjąć tych wartości."
        super().__init__(message)

class BladMnozenia(BladMatematyczny):
    def __init__(self, a, b):
        message = f"Błąd podczas mnożenia {a} i {b}. Nie można pomnożyć tych wartości."
        super().__init__(message)

class BladDzielenia(BladMatematyczny):
    def __init__(self, a, b):
        message = f"Błąd podczas dzielenia {a} przez {b}. Nie można dzielić przez zero."
        super().__init__(message)


def wykonaj_dzialanie(a, b, operacja):
    try:
        if operacja == '+':
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise BladDodawania(a, b)
            return a + b
        elif operacja == '-':
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise BladOdejmowania(a, b)
            return a - b
        elif operacja == '*':
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise BladMnozenia(a, b)
            return a * b
        elif operacja == '/':
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise BladDzielenia(a, b)
            if b == 0:
                raise BladDzielenia(a, b)
            return a / b
        else:
            raise BladMatematyczny("Nieznana operacja matematyczna.")
    except BladMatematyczny as e:
        return f"Błąd matematyczny: {e}"

# Przykład użycia funkcji
# print(wykonaj_dzialanie(5, 0, '/'))  # Symulacja błędu dzielenia przez zero
# print(wykonaj_dzialanie(10, 'abc', '+'))  # Symulacja błędu dodawania nieprawidłowych typów\
# print(wykonaj_dzialanie(15, 'abc', '-'))  # Symulacja błędu odejmowania nieprawidłowych typów
# print(wykonaj_dzialanie(15, 'xyz', '*'))  # Błąd mnożenia nieprawidłowych typów
# print(wykonaj_dzialanie(5, 2, '%'))  # Błąd matematyczny - nieznana operacja
# print(wykonaj_dzialanie(8, 4, '*'))  # Poprawne mnożenie


# Przykład 4
# Definicja klasy wyjątku
class MoWyjatek(Exception):
    def __init__(self, message="Wystąpił mój wyjątek"):
        self.message = message
        super().__init__(self.message)


# Funkcja używająca wyjątku
def moja_funkcja(tekst):
    try:
        if not tekst:
            raise MoWyjatek("Tekst nie może być pusty!")
        else:
            print("Podany tekst:", tekst)
    except MoWyjatek as e:
        print("Złapano wyjątek:", e)

# Przykładowe użycie funkcji
# moja_funkcja("Hello, World!")
# moja_funkcja("")  # Spowoduje wystąpienie wyjątku



# Przykład 5
class AktualnyCzas:
    def __init__(self):
        pass

    def pobierz_aktualny_czas(self):
        # Pobieranie aktualnego czasu w strefie czasowej lokalnej
        czas_lokalny = datetime.now()

        return czas_lokalny

# Przykładowe użycie
# czas_obj = AktualnyCzas()
# aktualny_czas = czas_obj.pobierz_aktualny_czas()
# print(f"Aktualny czas: {aktualny_czas}")


# Przykład 6

class AktualnyCzas:
    def __init__(self, miasto):
        self.miasto = miasto

    def pobierz_aktualny_czas(self):
        # Ustalanie strefy czasowej na podstawie nazwy miasta
        strefa_czasowa = timezone(self.miasto)

        # Pobieranie aktualnego czasu w danej strefie czasowej
        czas_w_strefie = datetime.now(strefa_czasowa)

        return czas_w_strefie

# Przykładowe użycie
# miasto = "America/Santiago"  # Strefa czasowa dla Warszawy
# czasownik = AktualnyCzas(miasto)
# aktualny_czas = czasownik.pobierz_aktualny_czas()
# print(f"Aktualny czas w {miasto}: {aktualny_czas}")