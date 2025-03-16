from threading import Thread
import requests
import time
import os

os.makedirs('nabor_sites_thread', exist_ok=True)

links = [
    "https://www.google.com",
    "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%88%D0%BA%D0%B0",
    "https://www.wikipedia.org",
    "https://github.com",
    "https://stackoverflow.com",
    "https://www.reddit.com",
    "https://habr.com",
    "https://chatgpt.com",
    'https://github.com/Seva5959',
    "https://www.nasa.gov"]
start_time = time.time()
def download(url: str):
    aboba = requests.get(url)
    file_name = 'threading_' + url.replace('https://','').replace('.','_').replace('/','_') + '.html'
    file_path = os.path.join('nabor_sites_thread', file_name)
    with open(file_path, mode='w', encoding='utf-8') as f:
        f.write(aboba.text)
    # print(f'Downloaded {url} in {time.time()-start_time:.2f} seconds')

def psevdo_main():
    start_time = time.time()
    threads = []
    for url in links:
        th = Thread(target=download, args=[url])
        threads.append(th)
        th.start()

    for thr in threads:
        thr.join()

    return round(time.time() - start_time, 3)















