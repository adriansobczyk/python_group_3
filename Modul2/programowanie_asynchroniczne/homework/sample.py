import asyncio
import aiohttp
from datetime import datetime, timedelta

API_URL = "https://api.nbp.pl/api/exchangerates/tables/a/"
TODAY = datetime.today().strftime("%Y-%m-%d")

async def get_rates(date):
    """Pobiera kursy walut dla danego dnia."""
    url = f"{API_URL}{date}?format=json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            elif response.status == 404:
                print(f"Brak danych dla dnia {date}")
                return None  # Zwrócenie None w przypadku braku danych
            else:
                raise RuntimeError(f"Błąd pobierania danych: {response.status}")

async def main(days):
    """Pobiera kursy walut dla kilku dni."""
    tasks = [get_rates((datetime.strptime(TODAY, "%Y-%m-%d") - timedelta(days=i)).strftime("%Y-%m-%d")) for i in range(days)]
    results = await asyncio.gather(*tasks)
    for i, result in enumerate(results, 1):
        print(f"Dane z dnia {datetime.strptime(TODAY, '%Y-%m-%d') - timedelta(days=i)}:")
        if result is not None:  # Sprawdź, czy wynik nie jest None
            for currency in result[0]["rates"]:
                print(f"{currency['currency']:4} {currency['code']:3} {currency['mid']:.4f}")
        print()


if __name__ == "__main__":
    try:
        days = int(input("Podaj liczbę dni (maksymalnie 10): "))
        if days > 10:
            raise ValueError("Liczba dni nie może być większa niż 10")
    except ValueError as e:
        print(f"Błąd: {e}")
    else:
        asyncio.run(main(days))
