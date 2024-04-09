import asyncio
import random

async def random_value():
    print("start task")
    await asyncio.sleep(1)
    print("task finished")
    return random.random()

async def main():
    # Tworzenie korutyny i zadania asynchronicznego
    task = asyncio.create_task(random_value())
    
    # Wyświetlanie komunikatu o zaplanowaniu zadania
    print("task scheduled")
    
    # Oczekiwanie na zakończenie zadania
    await task
    
    # Wyświetlanie wyniku zadania
    print(f"result: {task.result()}")


if __name__ == '__main__':
    asyncio.run(main())
