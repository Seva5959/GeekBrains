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

os.makedirs("nabor_sites_async", exist_ok=True)

async def download(session, url):
    async with session.get(url) as response:
        html = await response.text()
        file_name = 'async_' + url.replace('https://', '').replace('.', '_').replace('/', '_') + '.html'
        file_path = os.path.join("nabor_sites_async", file_name)
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(html)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [download(session, url) for url in links]
        await asyncio.gather(*tasks)

def psevdo_main():
    start_time = time.time()
    asyncio.run(main())
    return round(time.time() - start_time, 3)


