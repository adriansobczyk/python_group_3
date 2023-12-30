'''
1. Praca z datą i godziną w Pythonie (datetime)
'''

from datetime import datetime, timedelta, timezone

# print(datetime.now())
# print(datetime.now().year)

def current_date_time_example():
    """
    Przykład uzyskiwania bieżącej daty i godziny za pomocą datetime.
    """
    obecna_data_i_godzina = datetime.now()
    return obecna_data_i_godzina


def current_date_time_example_seperated(data):
    """
    Funkcja rozbijająca obiekt datetime na listę [rok, miesiąc, dzień, godzina, minuta, sekunda].

    Parameters:
    - data (datetime): Obiekt datetime do rozbicia.

    Returns:
    - list: Lista [rok, miesiąc, dzień, godzina, minuta, sekunda].
    """
    if not isinstance(data, datetime):
        raise ValueError("Parametr musi być obiektem datetime.")

    lista_daty = [
        f"Rok: {data.year}",
        f"Miesiąc: {data.month}",
        f"Dzień: {data.day}",
        f"Godzina: {data.hour}",
        f"Minuta: {data.minute}",
        f"Sekunda: {data.second}"
    ]

    return '\n'.join(lista_daty)


def date_operations_example():
    """
    Przykład operacji na dacie za pomocą datetime.
    """
    siódmy_dzień_2020 = datetime(year=2020, month=1, day=7, hour=14)
    print(siódmy_dzień_2020.year)


def calculate_interval_between_events(data_zdarzenia1, data_zdarzenia2):
    """
    Funkcja obliczająca interwał czasowy między dwoma zdarzeniami.

    Parameters:
    - data_zdarzenia1 (datetime): Pierwsza data i godzina zdarzenia.
    - data_zdarzenia2 (datetime): Druga data i godzina zdarzenia.

    Returns:
    - timedelta: Interwał czasowy między dwoma zdarzeniami.
    """
    if not isinstance(data_zdarzenia1, datetime) or not isinstance(data_zdarzenia2, datetime):
        raise ValueError("Podane parametry muszą być obiektami datetime.")

    # Obliczenie interwału między zdarzeniami
    interwal = data_zdarzenia2 - data_zdarzenia1
    return interwal


def display_week_day(data):
    """
    Funkcja określająca dzień tygodnia dla danej daty.

    Parameters:
    - data (datetime): Data do sprawdzenia.

    Returns:
    - str: Nazwa dnia tygodnia.
    """
    if not isinstance(data, datetime):
        raise ValueError("Podany parametr musi być obiektem datetime.")

    # Pobranie nazwy dnia tygodnia
    nazwa_dnia = data.strftime("%A")
    return nazwa_dnia


def is_leap_year(rok):
    """
    Funkcja sprawdzająca, czy rok jest przestępny.

    Parameters:
    - rok (int): Rok do sprawdzenia.

    Returns:
    - bool: True, jeśli rok jest przestępny, False w przeciwnym razie.
    """
    if not isinstance(rok, int):
        raise ValueError("Podany parametr musi być liczbą całkowitą.")

    # Sprawdzenie, czy rok jest przestępny
    return (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)


def compare_dates_only(data1, data2):
    """
    Funkcja porównująca daty bez uwzględniania godzin, minut i sekund.

    Parameters:
    - data1 (datetime): Pierwsza data do porównania.
    - data2 (datetime): Druga data do porównania.

    Returns:
    - int: 0, jeśli daty są równe; liczba ujemna, jeśli data1 jest wcześniejsza;
      liczba dodatnia, jeśli data1 jest późniejsza.
    """
    if not isinstance(data1, datetime) or not isinstance(data2, datetime):
        raise ValueError("Oba parametry muszą być obiektami datetime.")

    # Porównanie dat bez godzin, minut i sekund
    data1_bez_czasu = datetime(data1.year, data1.month, data1.day)
    data2_bez_czasu = datetime(data2.year, data2.month, data2.day)

    return (data1_bez_czasu - data2_bez_czasu).total_seconds()


def compare_dates_with_hours(data1, data2):
    """
    Funkcja porównująca dwie daty i godziny.

    Parameters:
    - data1 (datetime): Pierwsza data do porównania.
    - data2 (datetime): Druga data do porównania.

    Returns:
    - int: 0, jeśli daty są równe, liczba dodatnia, jeśli data1 jest późniejsza,
           liczba ujemna, jeśli data1 jest wcześniejsza niż data2.
    """
    if not isinstance(data1, datetime) or not isinstance(data2, datetime):
        raise ValueError("Oba parametry muszą być obiektami datetime.")

    if data1 == data2:
        return 0
    elif data1 > data2:
        return 1
    else:
        return -1


def check_if_summer_time():
    """
    Funkcja sprawdzająca, czy obecnie obowiązuje czas letni czy zimowy w Polsce,
    oraz zwracająca aktualną godzinę i dzień.

    Returns:
        dict: Słownik zawierający informacje o czasie letnim, aktualnej godzinie i dniu.
            Klucze:
            - 'czas_letni': True, jeśli obowiązuje czas letni, False w przeciwnym razie.
            - 'godzina': Aktualna godzina w formacie HH:MM.
            - 'dzien': Aktualny dzień w formacie RRRR-MM-DD.
    """
    # Pobierz aktualną datę i godzinę
    obecna_data = datetime.now()
    # obecna_data = datetime(year=2023, month=12, day=1, hour=12)

    # Określ daty rozpoczęcia i zakończenia czasu letniego w Polsce
    czas_letni_start = datetime(obecna_data.year, 3, 26)  # ostatnia niedziela marca
    czas_letni_end = datetime(obecna_data.year, 10, 29)  # ostatnia niedziela października

    # Sprawdź, czy obecna data mieści się w okresie czasu letniego
    if czas_letni_start <= obecna_data <= czas_letni_end:
        czas_letni = True
    else:
        czas_letni = False

    # Dodaj 1 godzinę, jeśli obowiązuje czas letni
    if czas_letni:
        obecna_data += timedelta(hours=1)

    # Zwróć wynik
    return {
        'czas_letni': czas_letni,
        'godzina': obecna_data.strftime('%H:%M'),
        'dzien': obecna_data.strftime('%Y-%m-%d'),
    }


def get_days_from_today(days):
    """
    Zwraca datę, która jest daną liczbę dni po dzisiejszej dacie.

    Args:
    - days (int): Liczba dni do przodu.

    Returns:
    - datetime: Obiekt daty.
    """
    try:
        # Dzisiejsza data
        dzisiejsza_data = datetime.now()

        # Obliczanie daty za daną liczbę dni
        przyszla_data = dzisiejsza_data + timedelta(days=days)

        return przyszla_data
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None


if __name__ == "__main__":
    # Przykładowe użycie funkcji current_date_time_example
    print(current_date_time_example())

    # Przykładowe użycie funkcji current_date_time_example_seperated
    obiekt_data = datetime(year=2024, month=1, day=1, hour=12, minute=30, second=45)
    wynik = current_date_time_example_seperated(obiekt_data)
    print("Rozbita lista daty:\n", wynik)

    # Przykładowe użycie funkcji date_operations_example
    date_operations_example()

    # Przykładowe użycie funkcji calculate_interval_between_events
    zdarzenie1 = datetime(year=2022, month=1, day=1, hour=12, minute=0)
    zdarzenie2 = datetime(year=2022, month=1, day=1, hour=15, minute=30)

    interwal_czasowy = calculate_interval_between_events(zdarzenie1, zdarzenie2)
    print(f"Interwał czasowy między zdarzeniem 1 a zdarzeniem 2: {interwal_czasowy}")

    # Przykładowe użycie funkcji display_week_day
    data_do_sprawdzenia = datetime(year=2022, month=1, day=1)
    dzien_tygodnia = display_week_day(data_do_sprawdzenia)
    print(f"Dzień tygodnia dla {data_do_sprawdzenia}: {dzien_tygodnia}")

    # Przykładowe użycie funkcji is_leap_year
    rok_do_sprawdzenia = 2024
    czy_przestepny = is_leap_year(rok_do_sprawdzenia)
    print(f"Czy rok {rok_do_sprawdzenia} jest przestępny? {czy_przestepny}")

    # Przykładowe użycie funkcji porównującej daty bez godzin, minut i sekund
    data1 = datetime(year=2022, month=1, day=1)
    data2 = datetime(year=2022, month=1, day=1)
    wynik_porownania = compare_dates_only(data1, data2)
    if wynik_porownania == 0:
        print("Daty są równe.")
    elif wynik_porownania < 0:
        print("Data 1 jest wcześniejsza niż Data 2.")
    else:
        print("Data 1 jest późniejsza niż Data 2.")

    # Przykładowe użycie funkcji compare_dates
    data_1 = datetime(year=2022, month=1, day=1, hour=12, minute=30)
    data_2 = datetime(year=2022, month=1, day=1, hour=10, minute=15)

    # wynik_porownania = compare_dates_with_hours(data_1, data_2)

    # if wynik_porownania == 0:
    #     print("Daty są równe.")
    # elif wynik_porownania > 0:
    #     print(f"{data_1} jest późniejsza niż {data_2}.")
    # else:
    #     print(f"{data_1} jest wcześniejsza niż {data_2}.")

    # Przykładowe użycie funkcji current_datetime_in_my_timezone
    # wynik = check_if_summer_time()
    # print("Czas letni:", "Tak" if wynik['czas_letni'] else "Nie")
    # print("Aktualna godzina:", wynik['godzina'])
    # print("Aktualny dzień:", wynik['dzien'])

    # Przykładowe użycie funkcji - pobranie daty za 60 dni od dzisiaj
    # wynik = get_days_from_today(60)
    # print("Data za 60 dni od dzisiaj:", wynik.strftime('%Y-%m-%d'))
