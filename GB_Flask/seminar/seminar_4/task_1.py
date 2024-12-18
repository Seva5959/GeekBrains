import requests
from threading import Thread
import time
import os

urls = [
    'https://youtube.com',
    'https://chatgpt.com',
    'https://mail.google.com',
    'https://github.com/Seva5959',
    'https://app.fengmyshui.com'
]


def downoload(url: str):
    response = requests.get(url)
    file_name = 'threading_' + url.replace('https://', '').replace('.','_').replace('/','_') + '.html'
    file_path = os.path.join('nabor_sites_task_1', file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

threads = []
start_time = time.time()
for url in urls:
    trhead = Thread(target=downoload,args=[url])
    threads.append(trhead)
    trhead.start()

for thread in threads: # без нее программа может закончится не вовремя
    thread.join()      # кароче важная штука









