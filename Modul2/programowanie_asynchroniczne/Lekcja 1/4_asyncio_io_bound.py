import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor
from time import time

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']

# Synchroniczna funkcja

def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]


if __name__ == '__main__':
    start = time()
    for url in urls:
        r = preview_fetch(url)
        print(r)
    print(time() - start)

# Asynchroniczna funkcja

def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]

async def preview_fetch_async():
    # Pobranie aktualnie działającej pętli zdarzeń asyncio
    loop = asyncio.get_running_loop()

    # Utworzenie executora wątków z maksymalnie 3 wątkami
    with ThreadPoolExecutor(3) as pool:
        # Utworzenie listy futures dla zadań asynchronicznych
        futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
        
        # Oczekiwanie na zakończenie wszystkich zadań i zebranie ich wyników
        # return_exceptions=True pozwala na zwrócenie wyjątków zamiast ich podnoszenia
        # *futures rozpakowuje listę futures na argumenty pozycyjne funkcji asyncio.gather
        result = await asyncio.gather(*futures, return_exceptions=True)
        
        # Zwrócenie wyników zadań asynchronicznych
        return result

if __name__ == '__main__':
    start = time()
    r = asyncio.run(preview_fetch_async())
    print(r)
    print(time() - start)

# Na Windows w niektórych przypadkach wymagane jest użycie ProactorEventLoop zamiast domyślnego SelectorEventLoop
# ze względu na ograniczenia systemu operacyjnego w obsłudze operacji wejścia/wyjścia asynchronicznych w wątkach Pythona
# https://docs.python.org/pl/3.6/library/asyncio-eventloops.html