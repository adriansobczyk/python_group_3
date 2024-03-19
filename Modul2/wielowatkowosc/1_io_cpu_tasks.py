'''
Zadania IO i CPU
'''
 
import time
import requests
import concurrent.futures

'''
GIL

+-----------------------------------------+
|             Python Interpreter          |
+-----------------------------------------+
|                   GIL                 <----+
+-----------------------------------------+   |
                                              |
+-----------------------------------------+   |
|            Wątek 1 (Thread 1)           |   |
+-----------------------------------------+   |
|             Kod Pythona                 |   |
|                ...                      |   |
|                ...                      |   |
|                ...                      |   |
+-----------------------------------------+   |
                                              |
+-----------------------------------------+   |
|            Wątek 2 (Thread 2)           |   |
+-----------------------------------------+   |
|             Kod Pythona                 |   |
|                ...                      |   |
|                ...                      |   |
|                ...                      |   |
+-----------------------------------------+   |
                                              |
                ...                           |
                                              |
+-----------------------------------------+   |
|            Wątek N (Thread N)           |   |
+-----------------------------------------+   |
|             Kod Pythona                 |   |
|                ...                      |   |
|                ...                      |   |
|                ...                      |   |
+-----------------------------------------+   |
                                              |
+-----------------------------------------+   |
|         Moduły i Obiekty Pythona        |   |
+-----------------------------------------+   |
                                              |
+-----------------------------------------+   |
|                 Proces                  |   |
+-----------------------------------------+---+
|             Interpreter Pythona         |   |
|                   GIL                   |   |
|            Wątek 1 (Thread 1)           |   |
|            Wątek 2 (Thread 2)           |   |
|            Wątek N (Thread N)           |   |
|         Moduły i Obiekty Pythona        |   |
|             System operacyjny (OS)      |   |
+-----------------------------------------+

'''


# CPU-bound task
def cpu_bound(number):
    '''
    Funkcja obciążająca procesor. Oblicza sumę kwadratów liczb od 0 do number.
    '''
    return sum(i * i for i in range(number))

def find_sums(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        print("Wątek główny: Rozpoczęcie obliczeń")
        executor.map(cpu_bound, numbers)
        print("Wątek główny: Zakończenie obliczeń")


# IO-bound task
def download_site(url):
    response = requests.get(url)
    print(f"Header from {url}:", response.headers)
    return response.headers

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":

    # CPU-bound task
    numbers = [1000000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Zadanie CPU trwało {duration} s.")

    # IO-bound task
    # sites = ["https://realpython.com/", "https://pl.wikipedia.org/wiki/Wiki"] * 1
    # start_time = time.time()
    # download_all_sites(sites)
    # duration = time.time() - start_time
    # print(f"Zadanie IO trwało {duration} s.")
