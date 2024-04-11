import asyncio
from time import sleep, time

# Event loop

async def say_hello(delay, name):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    # Tworzymy listę zadań do wykonania
    tasks = [
        say_hello(1, "Alice"),
        say_hello(2, "Bob"),
        say_hello(3, "Charlie")
    ]
    # Uruchamiamy event loop i czekamy na zakończenie wszystkich zadań
    await asyncio.gather(*tasks)

# # Uruchamiamy główną funkcję wewnątrz event loop
# asyncio.run(main())

# Async oraz await

# async def bar():
#     await asyncio.sleep(2) # await służy do oczekiwania na zakończenie innej korutyny
#     print("Zakończono bar")

# async def baz():
#     await asyncio.sleep(1)
#     print("Zakończono baz")

# async def main():
#     print("Rozpoczęto main")
#     await baz()
#     await bar()
#     print("Zakończono main")

# asyncio.run(main())


# Przykład 1

# async def fetch_data(url):
#     print("Fetching data from:", url)
#     await asyncio.sleep(1)
#     return "Data from " + url

# async def main():
#     task1 = asyncio.create_task(fetch_data("https://api.sampleapis.com/codingresources/codingResources"))
#     task2 = asyncio.create_task(fetch_data("https://api.sampleapis.com/switch/games"))

#     data1 = await task1
#     data2 = await task2

#     print("Data 1:", data1)
#     print("Data 2:", data2)

# asyncio.run(main())

# Przykład 2

# async def baz() -> str:
#     print('Before Sleep')
#     await asyncio.sleep(1)
#     print('After Sleep')
#     return 'Hello world'

# async def main():
#     r = baz()  # Uruchomienie korutyny
#     print(r)   # Wyświetlenie obiektu Future
#     result = await r  # Oczekiwanie na zakończenie korutyny
#     print(result)

# if __name__ == '__main__':
#     asyncio.run(main())  # Uruchomienie pętli zdarzeń i głównej korutyny

# Przykład 3

# fake_users = [
#     {'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc', 'email': 'shawnlittle@example.org'},
#     {'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith', 'email': 'turnerandrew@example.org'},
#     {'id': 3, 'name': 'Patrick Jones', 'company': 'Young, Pruitt and Miller', 'email': 'alancoleman@example.net'}
# ]

# def get_user_sync(uid: int) -> dict:
#     sleep(0.5)
#     user, = list(filter(lambda user: user["id"] == uid, fake_users))
#     return user

# if __name__ == '__main__':
#     start = time()
#     for i in range(1, 4):
#         print(get_user_sync(i))
#     print(time() - start)

# Przykład 4

# fake_users = [
#     {'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc', 'email': 'shawnlittle@example.org'},
#     {'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith', 'email': 'turnerandrew@example.org'},
#     {'id': 3, 'name': 'Patrick Jones', 'company': 'Young, Pruitt and Miller', 'email': 'alancoleman@example.net'}
# ]

# async def get_user_async(uid: int) -> dict:
#     await asyncio.sleep(0.5)
#     user, = list(filter(lambda user: user["id"] == uid, fake_users))
#     return user

# async def main():
#     r = []
#     for i in range(1, 4):
#         r.append(get_user_async(i))
#     return await asyncio.gather(*r)

# if __name__ == '__main__':
#     start = time()
#     result = asyncio.run(main())
#     for r in result:
#         print(r)
#     print(time() - start)
