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
    "https://www.nasa.gov"
]


def download(url: str):
    start_time = time.time()  # Начало отсчёта времени внутри процесса
    response = requests.get(url)

    os.makedirs("nabor_sites_for_task_2", exist_ok=True)  # Создаём папку, если её нет

    file_name = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '_') + '.html'
    file_path = os.path.join("nabor_sites_for_task_2", file_name)

    with open(file_path, mode='w', encoding='utf-8') as f:
        f.write(response.text)

    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


if __name__ == "__main__":
    start_time = time.time()

    with Pool(processes=os.cpu_count()) as pool:
        pool.map(download, links)

    print(f"Finished in {time.time() - start_time:.2f} seconds")
