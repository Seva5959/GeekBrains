import asyncio
import aiohttp
import time
import os

urls = [
    'https://youtube.com',
    'https://chatgpt.com',
    'https://mail.google.com',
    'https://github.com/Seva5959',
    'https://app.fengmyshui.com'
]

start_time = time.time()
async def download(url):
    async with aiohttp.ClientSession()as session:
        async with  session.get(url) as response:
            text = await response.text()
    file_name = 'asyncio_' + url.replace('htpps://', '').replace('.', '_').replace('/','') + '.html'
    file_path = os.path.join('sites_for_4_task' + file_name)
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(text)
        print(f'Download {url} in {time.time() - start_time: .2f} seconds ')

async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
        await asyncio.gather(*task)


if __name__ == '__main__':
    loop = asyncio.get_running_loop()
    loop.run_until_complete(main())