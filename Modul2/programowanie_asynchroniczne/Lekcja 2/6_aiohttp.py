import platform
import aiohttp
import asyncio

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.google.com/') as response:
#             html = await response.text()
#             print(html)

# if __name__ == '__main__':
#     asyncio.run(main())


# async def main():

#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://python.org') as response:

#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])

#             html = await response.text()
#             print("Body:", html[:15], "...")

# if __name__ == "__main__":
#     if platform.system() == 'Windows':
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#     asyncio.run(main())
