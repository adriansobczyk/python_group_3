import asyncio
import concurrent.futures
from time import time


def blocks(n):
    counter = n
    start = time()
    while counter > 0:
        counter -= 1
    return time() - start


async def monitoring():
    while True:
        await asyncio.sleep(2)
        print(f'Monitoring {time()}')


async def run_blocking_tasks(executor, n):
    loop = asyncio.get_event_loop()
    print('waiting for executor tasks')
    result = await loop.run_in_executor(executor, blocks, n)
    return result


async def main():
    # Tworzymy korutynę do monitorowania
    asyncio.create_task(monitoring())

    # Tworzymy executor wątków
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Tworzymy listę futures dla blokujących operacji z różnymi wartościami n
        futures = [run_blocking_tasks(executor, n) for n in [50_000_000, 60_000_000, 70_000_000]]
        
        # Oczekujemy na zakończenie wszystkich futures i zbieramy ich wyniki
        results = await asyncio.gather(*futures)
        return results



if __name__ == '__main__':
    result = asyncio.run(main())
    for r in result:
        print(r)
