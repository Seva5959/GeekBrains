# task_3
import asyncio
import aiohttp
import os
import time


links = [
    "https://www.google.com",
    "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0",
    "https://www.wikipedia.org",
    "https://github.com",
    "https://stackoverflow.com",
    "https://www.reddit.com",
    "https://habr.com",
    "https://chatgpt.com",
    "https://github.com/Seva5959",
    "https://www.nasa.gov"
]

# Создаём папку, если её нет
os.makedirs("nabor_sites_async", exist_ok=True)

start_time = time.time()
async def download(session, url):
    """Функция для асинхронной загрузки страницы."""
    start_time = time.time()

    async with session.get(url) as response:
        html = await response.text() # await используем всегда перед долгим сигналом

            # Формируем имя файла
        file_name = 'async_' + url.replace('https://', '').replace('.', '_').replace('/', '_') + '.html'
        file_path = os.path.join("nabor_sites_async", file_name)

            # Сохраняем страницу в файл
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(html)
            # print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')

async def main():
    """Основная асинхронная функция."""
    async with aiohttp.ClientSession() as session:
        tasks = [download(session, url) for url in links]
        await asyncio.gather(*tasks)  # Запускаем все загрузки одновременно


def psevdo_main():
    print('psevdo_main')
    # Запускаем асинхронный код
    asyncio.run(main())
    # print(f"Finished in {time.time() - start_time:.2f} seconds")
    end_time = time.time() - start_time
    return round(end_time,3)

