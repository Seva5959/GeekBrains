import asyncio
import os
import aiofiles
import time

start_time = time.time()
async def count_word(file_path, q):
    async with aiofiles.open(file_path, mode='r', encoding='utf-8') as f:
        txt = await f.read()
        len_rez = len(txt.split())
    await q.put((file_path, len_rez))


async def main(path_dire):
    tasks = []
    q = asyncio.Queue()
    for filename in os.listdir(path_dire):
        file_path = os.path.join(path_dire, filename)
        if os.path.isfile(file_path):
            tasks.append(count_word(file_path, q))
    await asyncio.gather(*tasks)

    while not q.empty():
        file, len_r = await q.get()
        print(len_r, file)


if __name__ == '__main__':
    asyncio.run(main('nabor_sites_thread'))
    print(f'\n{time.time()-start_time:.2f}')