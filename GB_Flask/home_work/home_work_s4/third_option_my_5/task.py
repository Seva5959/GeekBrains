import urllib.parse
import tqdm
import os
import bs4
import requests
import magic

name_sitec = ''
site = 'https://ca.pinterest.com/ideas/%D1%84%D0%BE%D1%82%D0%BE-%D0%BD%D0%B0-%D0%B0%D0%B2%D1%83-%D1%81-%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B0%D0%BC%D0%B8/947752823216/'
dict_ext = {'image/jpeg': '.jpeg',
            'image/png': '.png',
            'image/gif': '.gif',
            'image/webp': '.webp',
            'image/svg': '.svg', }
direction = 'storage'


def get_all_src(link: str) -> list[str]:
    urls = []
    soup = bs4.BeautifulSoup(requests.get(link).content, 'html.parser')  # В случае ошибки посмотреть сюда
    for img in tqdm.tqdm(iterable=soup.find_all('img'), desc='Извлекаю из img src:'):
        img_src = img.attrs.get('src')
        if not img_src:
            continue
        img_url = urllib.parse.urljoin(link, img_src)

        if '?' in img_url:
            img_url = img_url.split('?')[0]
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def is_valid(link: str) -> bool:
    parsed = urllib.parse.urlparse(link)
    return bool(parsed.scheme) and bool(parsed.netloc)

def downloader_img(link: str, direction_to_save: str, count: int ) -> None:
    with requests.get(link, stream=True) as response:
        if response.status_code != 200










