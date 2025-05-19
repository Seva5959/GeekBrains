import bs4
import os
import requests
import tqdm
import urllib.parse

def get_src_imgs(url_site: str) -> list[str]:
    '''
    Функция собирает все src img с указанного сайта и возращает список валидных ссылок
    на файлы
    Args:
        url_site: str - Ссылка на сайт
    Returns:
        list[str] - Список обсолютных валидных ссылок
    '''
    urls = []
    soup = bs4.BeautifulSoup(requests.get(url_site).content, 'html.parser')
    for img in tqdm.tqdm(iterable=soup.find_all('img'), desc='Извлекаю все изображения'):
        url_img = img.attrs.get('src')
        if not url_img:
            continue
        full_img_url = urllib.parse.urljoin(url_site, url_img)

        if '?' in full_img_url:
            full_img_url = full_img_url.split('?')[0]
        if url_is_valid(full_img_url):
            urls.append(full_img_url)

    return urls


def url_is_valid(url: str):
    '''
    Функция проверяет валидность ссылки
    Args:
        url: str - URL-адрес
    Returns:
        Возращает True - если есть протокол(scheme) и домен(netloc)
        Возращает False - если нет или протокола(scheme) или домена(netloc)
    '''
    parsed = urllib.parse.urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)