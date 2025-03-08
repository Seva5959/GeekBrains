from threading import Thread
import requests
import time
import os

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
    file_path = os.path.join('nabor_sites_for_task_1', file_name)
    with open(file_path, mode='w', encoding='utf-8') as f:
        f.write(aboba.text)
    print(f'Downloaded {url} in {time.time()-start_time:.2f} seconds')

threads = []
for url in links:
    th = Thread(target=download, args=[url])
    threads.append(th)
    th.start()

for thr in threads:
    thr.join()















