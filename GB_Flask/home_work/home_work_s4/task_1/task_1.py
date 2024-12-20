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

def time_decor(func):
    def wrapper(*args, **kwargs):
        start_t = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Result: {result} It took {finish-start_t:.2f} seconds')
    return wrapper

@time_decor
def download(url):
    respon = requests.get(url)
    file_name = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '_') + '.html'
    file_path = os.path.join('nabor_sites_task_1', file_name)
    with open(file_path, 'w', encoding='utf-8')as f:
        f.write(respon.text)
    return f'{url} succes load!'


def potok():
    threads = []
    for url in urls:
        trhead = Thread(target=download, args=[url])
        threads.append(trhead)
        trhead.start()

    for thread in threads:  # без нее программа может закончится не вовремя
        thread.join()  # кароче важная штука

potok()