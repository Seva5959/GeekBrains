import threading
from threading import Thread
import os
import time
import requests

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

os.makedirs('nabor_sites_thread_02', exist_ok=True)
def download(url: str):
    html_sitec = requests.get(url)
    file_name = 'threading_' + url.replace('https://','').replace('.','_').replace('/','_') + '.html'
    file_path = os.path.join('nabor_sites_thread_02', file_name)
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(html_sitec.text)

start_time = time.time()
threads = []
for link in links:
    task = threading.Thread(target=download, args=[link])
    threads.append(task)
    task.start()


    for th in threads:
        th.join()

print(time.time() - start_time)





