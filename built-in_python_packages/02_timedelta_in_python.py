'''
2. timedelta w Pythonie
Moduł timedelta w Pythonie jest używany do reprezentowania różnicy między dwoma datami lub czasami.
'''

from datetime import timedelta, datetime

def timedelta_example():
    """
    Przykłady tworzenia obiektów timedelta.
    """
    # Tworzenie obiektu timedelta
    delta = timedelta(days=50, hours=25, minutes=20, seconds=30)
    return delta


def timedelta_creation(tygodnie=0, dni=0, godziny=0, minuty=0, sekundy=0):
    """
    Tworzy obiekt timedelta na podstawie podanych wartości.

    Args:
    - tygodnie (int): Liczba tygodni (domyślnie 0).
    - dni (int): Liczba dni (domyślnie 0).
    - godziny (int): Liczba godzin (domyślnie 0).
    - minuty (int): Liczba minut (domyślnie 0).
    - sekundy (int): Liczba sekund (domyślnie 0).

    Returns:
    - timedelta: Obiekt timedelta.
    """
    delta = timedelta(weeks=tygodnie, days=dni, hours=godziny, minutes=minuty, seconds=sekundy)
    return delta


def add_n_weeks(do_daty_str, liczba_tygodni):
    """
    Dodaje określoną liczbę tygodni do danej daty.

    Args:
    - do_daty_str (str): Data początkowa w formacie "YYYY-MM-DD".
    - liczba_tygodni (int): Liczba tygodni do dodania.

    Returns:
    - str: Data po dodaniu określonej liczby tygodni.
    """
    data_poczatkowa = datetime.strptime(do_daty_str, "%Y-%m-%d")
    data_po_dodaniu = data_poczatkowa + timedelta(weeks=liczba_tygodni)
    
    return data_po_dodaniu.strftime("%Y-%m-%d")


if __name__ == "__main__":
    # Przykłady tworzenia obiektów timedelta
    delta = timedelta_example()
    print(f"Utworzony timedelta: {delta}")
    # Tworzenie timedelta
    delta_przyklad = timedelta_creation(tygodnie=1, dni=5, godziny=3, minuty=4, sekundy=5)
    print(f"Utworzony timedelta: {delta_przyklad}")
    # Dodawanie timedelta do daty
    data_poczatkowa_str = "2024-01-02"
    liczba_tygodni = 4
    nowa_data = add_n_weeks(data_poczatkowa_str, liczba_tygodni)
    print(f"Nowa data po dodaniu 4 tygodni: {nowa_data}")
