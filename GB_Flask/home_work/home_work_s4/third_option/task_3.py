import os
import requests
import tqdm
import bs4
import urllib.parse

site_name = 'https://www.nasa.gov/'
dir_for_images = 'storage'

def get_all_images(url: str) -> list[str]:
    '''
    Функция проходит по сайту и берет оттуда src. После чего преобразует в ссылку для скачивания

    The function goes through the site and takes the src from there. Then it converts it into a download link.
    '''
    # Позволяет, получить объект из которого удобно достать любой html тег
    soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser')
    urls = []
    # Обычный for i in range, но тут есть прогресс бар.
    # Важно учитывать, что в асинхронном коде это может работать некорректно.
    # Лучше использовать tqdm.asyncio
    for img in tqdm.tqdm(iterable=soup.find_all('img'), desc='Извлечение изображений'):
        # attrs превращает img (условно "str") в условно "словарь", где
        # src и alt ключи, а остальное значение
        img_url = img.attrs.get('src')
        # Бывают ленивые загрузки. Img загружаются непосредственно, когда пользователь доскролил
        # Поэтому они не лежат стандартно в теге <img>
        if not img_url:
            continue
        # Отрабатывает относительные пути по типу 1)/img/logo.png 2)/assets/img.jpg 3)images/pic.png
        # Соединяя их с основной ссылкой для скачивания
        img_url = urllib.parse.urljoin(url, img_url)
        # Часто сайты добавляют после разрешения файла "?" для обхода кэша
        # В таком случае, браузер гарантировано обновит изображении, так как считает его новым, а
        # не будет брать его из кэша
        if '?' in img_url:
            img_url = img_url.split('?')[0]
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def is_valid(url: str) -> bool:
    '''
    Функция проверяет, есть ли у ссылки домен и протокол

    The function checks if the link has a domain and protocol.
    '''
    parsed = urllib.parse.urlparse(url)
    # Библиотека urllib позволяет удобно работать с url, разбивая его на нужные фрагменты
    # parsed.scheme — это протокол (например: http, https, ftp)
    # parsed.netloc — это домен (например: example.com, nasa.gov)
    return bool(parsed.netloc) and bool(parsed.scheme)


def download(url: str, name_dir: str, count: int) -> None:
    '''
    Функция скачивает изображение в указанную директорию

    The function downloads the image to the specified directory
    '''
    os.makedirs(name_dir, exist_ok=True)
    response = requests.get(url, stream=True)
    # splitext предназначен для того, чтобы разбивать url на окончание и все остальное
    ext = os.path.splitext(url)[1]
    filename = os.path.join(name_dir, f'foto_{count}{ext}')
    file_size = int(response.headers.get('Content-Length', 0))
    progress = tqdm.tqdm(response.iter_content(1024), f'Загрузка {filename}',
        total=file_size, unit='B', unit_scale=True, unit_divisor=1024)
    with open(filename, mode='wb')as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))


def main(url: str, path: str) -> None:
    count = 0
    imgs = get_all_images(url)
    for img in imgs:
        count += 1
        download(img, path, count)


main(site_name, dir_for_images)


















