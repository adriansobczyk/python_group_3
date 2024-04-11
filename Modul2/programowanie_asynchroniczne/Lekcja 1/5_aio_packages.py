import asyncio
from aiofile import async_open
from aiopath import AsyncPath
from aioshutil import copyfile

# Aiofile - async for
# async def main():
#     async with async_open("hello.txt", 'w+') as afp:
#         await afp.write("Hello ")
#         await afp.write("world\n")
#         await afp.write("Hello from - async world!")

# if __name__ == '__main__':
#     asyncio.run(main())

# Aiofile - await afp.read()
# async def main():
#     async with async_open("hello.txt", 'r') as afp:
#         print(await afp.read())

# if __name__ == '__main__':
#     asyncio.run(main())


# Aiopath
# async def main():
#     apath = AsyncPath("hello.txt")
#     print(await apath.exists())
#     print(await apath.is_file())
#     print(await apath.is_dir())

# if __name__ == '__main__':
#     asyncio.run(main())

# Aioshutil
# async def main():
#     apath = AsyncPath("hello.txt")
#     if await apath.exists():
#         new_path = AsyncPath('logs')
#         await new_path.mkdir(exist_ok=True, parents=True)
#         await copyfile(apath, new_path / apath)

# if __name__ == '__main__':
#     asyncio.run(main())

