import os
import requests
import tqdm
import bs4
import urllib.parse

site_name = 'https://www.nasa.gov/'
dir_for_images = 'storage'

def get_all_images(url: str) -> list[str]:
    # Позволяет, получить объект из которого удобно достать любой html тег
    soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser')
    urls = []
    # Обычный for i in range, но тут есть прогресс бар.
    # Важно учитывать, что в асинхронном коде это может работать некорректно.
    # Лучше использовать tqdm.asyncio
    for img in tqdm.tqdm(iterable=soup.find_all('img'), desc='Извлечение изображений'):
        img_url = img.attrs.get('src')
        if not img_url:
            continue
        img_url = urllib.parse.urljoin(url, img_url)
        try:
            pos = img_url.index('?')
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def is_valid(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def download(url: str, name_dir: str) -> None:
    os.makedirs(name_dir, exist_ok=True)
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('Content-Length', 0))
    filename = os.path.join(name_dir, url.split('/')[-1])

    progress = tqdm.tqdm(response.iter_content(1024), f'Загрузка {filename}',
        total=True, unit='B', unit_scale=True, unit_divisor=1024)
    with open(filename, mode='wb')as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))


def main(url: str, path: str) -> None:
    imgs = get_all_images(url)
    for img in imgs:
        download(img, path)


main(site_name, dir_for_images)


















