import asyncio

async def print_numbers(): # async встроенное ключевое слово в пайтон.
    # Используется также в других случаях
    for i in range(10):
        print(i)
        await asyncio.sleep(1) # await аналогичен async. Тоже предустановленное слово пайтон


async def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        print(letter)
        await asyncio.sleep(0.5)

async def main():
    task_1 = asyncio.create_task(print_numbers())
    task_2 = asyncio.create_task(print_letters())
    await task_1
    await task_2


asyncio.run(main())











