import urllib.parse
import tqdm
import os
import bs4
import requests
import magic

site = 'https://ca.pinterest.com/ideas/%D1%84%D0%BE%D1%82%D0%BE-%D0%BD%D0%B0-%D0%B0%D0%B2%D1%83-%D1%81-%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B0%D0%BC%D0%B8/947752823216/'
dict_ext = {'image/jpeg': '.jpeg',
            'image/png': '.png',
            'image/gif': '.gif',
            'image/webp': '.webp',
            'image/svg': '.svg', }
direction = 'storage'


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


def download_file_from_site(url: str, direction: str, count: int) -> None:
    '''
    Функция скачивает файл с данного url в указанную директорию
    Args:
        url: str - Ссылка на файл
        direction: str - Директория для сохранения файла
        count: int - Число для имени файла. Подразумевается, что функция будет итерироваться и для
        уникального имени необходимо добавить число
    Returns:
        None - Функция ничего не возращает, но скачивает файл на диск
    '''

    os.makedirs(direction, exist_ok=True)
    with requests.get(url, stream=True) as response:
        if response.status_code != 200:
            raise Exception('Файл не найден')
        file_size = int(response.headers.get('Content-Length', 0))
        first_chunk = next(response.iter_content(1024 * 10))
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(first_chunk)
        if mime_type not in dict_ext:
            print(f"Пропускаем файл с типом {mime_type}, не поддерживаемый.")
            return

        extension = dict_ext[mime_type]
        full_name_file = os.path.join(direction, f'file_{count}.{extension}')

        with open(full_name_file, mode='wb') as f:
            f.write(first_chunk)
            progress = tqdm.tqdm(total=file_size, unit='B', unit_scale=True,
                                 desc=f'Скачиваю {file_size}')
            for chunk in response.iter_content(1024 * 10):
                if chunk:
                    f.write(chunk)
                    progress.update(len(chunk))


def main(url: str, dire: str) -> None:
    '''
    Функция очищает директорию перед загрузкой файлов. После вызывает основную логику скачивания
    Args:
        url: str - Ссылка на сайт, с которого нужно скачать файлы
        dire: str - Директория для скачивания
    Returns:
        Ничего не возращает
    '''
    for file in os.listdir(dire):
        path_file = os.path.join(dire, file)
        os.unlink(path_file)

    count = 0
    url_files = get_all_src_imgs(url)
    for url_file in url_files:
        count += 1
        download_file_from_site(url_file, dire, count)


if __name__ == '__main__':
    main(site, direction)
