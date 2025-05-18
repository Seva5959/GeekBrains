import urllib.parse
import tqdm
import os
import bs4
import requests

site = ''


def get_all_src_imgs(url: str) -> list[str]:
    """
    Функция проходит по сайту и собирает все src относящихся к img.

    Args:
        url: str - Ссылка на сайт, для которого нужно получить ссылки на изображения
    Returns:
        list[str] - Список валидных ссылок
    """

    urls = []
    soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser')
    for img in tqdm.tqdm(iterable=soup.find_all('img'), desc='Извлекаю тег img:'):
        img_url = img.attrs.get('src')
        if not img_url:
            continue
        img_url = urllib.parse.urljoin(url, img_url)

        if '?' in img_url:
            img_url = img_url.split('?')[0]
        if url_is_valid(img_url):
            urls.append(img_url)

    return urls


def url_is_valid(url: str) -> bool:
    '''
    Функция проверяет есть ли протокол и домен протокол у ссылки

    Args:
        url: str - Ссылка, у которой нужно проверить
    Returns:
        bool: True: Если ссылка имеет протокол(scheme) и домен(netloc)
              False:
    '''
    parsed = urllib.parse.urlparse(url)
    return bool(parsed.scheme) and bool(parsed.netloc)
