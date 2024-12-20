# декоратор не работает с мултипроцессорным способом
import requests
from multiprocessing import Process, freeze_support
import time
import os

urls = [
    'https://youtube.com',
    'https://chatgpt.com',
    'https://mail.google.com',
    'https://github.com/Seva5959',
    'https://app.fengmyshui.com'
]
res_lst = []
def time_decor(func):
    def wrapper(*args, **kwargs):
        global res_lst
        start_t = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        txt = f'Result: {result} It took {finish-start_t:.2f} seconds'
        res_lst.append(txt)
    return wrapper

# @time_decor
def download(url):
    respon = requests.get(url)
    file_name = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '_') + '.html'
    file_path = os.path.join('nabor_sites_task_1', file_name)
    with open(file_path, 'w', encoding='utf-8')as f:
        f.write(respon.text)
    return f'{url} succes load!'


def working_method():
    process_lst = []
    for url in urls:
        process = Process(target=download, args=(url,))
        process_lst.append(process)
        process.start()

    for process in process_lst:
        process.join()
    return res_lst



if __name__ == '__main__':
    working_method()