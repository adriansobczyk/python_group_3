'''
3. Timestamp
Timestamp to liczba sekund, która upłynęła od 1 stycznia 1970 roku. Timestamp jest używany do przechowywania daty i czasu. 
Timestamp jest używany w wielu systemach informatycznych, np. w systemach baz danych.
'''

from datetime import datetime

def timestamp_example():
    """
    Przykład tworzenia timestampu.
    """
    # Tworzenie timestampu
    timestamp = datetime.timestamp(datetime.now())
    return timestamp


def timestamp_to_datetime(timestamp):
    """
    Zamienia timestamp na datę i czas.

    Args:
    - timestamp (float): Timestamp.

    Returns:
    - datetime: Data i czas.
    """
    data_i_czas = datetime.fromtimestamp(timestamp)
    return data_i_czas


def datetime_to_timestamp(data_i_czas):
    """
    Zamienia datę i czas na timestamp.

    Args:
    - data_i_czas (datetime): Data i czas.

    Returns:
    - float: Timestamp.
    """
    timestamp = datetime.timestamp(data_i_czas)
    return timestamp


if __name__ == "__main__":
    # Przykład tworzenia timestampu
    timestamp = timestamp_example()
    print(f"Utworzony timestamp: {timestamp}")
    # Zamiana timestampu na datę i czas
    data_i_czas = timestamp_to_datetime(timestamp)
    print(f"Data i czas: {data_i_czas}")
    # Zamiana daty i czasu na timestamp
    timestamp = datetime_to_timestamp(data_i_czas=datetime(year=2024, month=1, day=2, hour=20, minute=0, second=0))
    print(f"Timestamp: {timestamp}")