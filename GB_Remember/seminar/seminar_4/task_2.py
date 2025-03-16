import time
import os
import requests
from multiprocessing import Pool


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

os.makedirs('nabor_sites_multipocess', exist_ok=True)
def download(url: str):
    aboba = requests.get(url)
    file_name = 'multipocess' + url.replace('https://','').replace('.','_').replace('/','_') + '.html'
    file_path = os.path.join('nabor_sites_multipocess', file_name)
    with open(file_path, mode='a', encoding='utf-8') as f:
        f.write(aboba.text)



# if __name__ == "__main__":
#     # Контекстный менеджер автоматически закроет все процессы, когда они завершат работу,
#     # не нужно делать pool.close() и pool.join() вручную.
#     with Pool(processes=os.cpu_count()) as pool: # кол-во процессов будет равно кол-ву ядер пк
#         pool.map(download, links)

def psevdo_main():
    """Измеряем время работы multiprocessing"""
    start_time = time.time()  # Засекаем время перед запуском пулла
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(download, links)
    end_time = time.time() - start_time  # Фиксируем разницу времени
    return round(end_time, 3)


if __name__ == "__main__":
    print(psevdo_main())  # Запускаем, если файл выполняется напрямую













