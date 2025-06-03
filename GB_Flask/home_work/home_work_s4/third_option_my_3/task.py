import os
import requests
import tqdm
import bs4
import urllib.parse
import magic

site_name = ''
dir_for_images = 'storage'
dict_ext = {'image/jpeg': '.jpeg',
            'image/png': '.png',
            'image/gif': '.gif',
            'image/webp': '.webp',
            'image/svg': '.svg', }

def get_all_image(url: str) -> list[str]:
    soup = bs4.BeautifulSoup(requests.get(url).content)
    urls = []
    for img in tqdm.tqdm(iterable=soup.find_all('img'), desc='Извлечение изображений'):
        img_url = img.attrs.get('src')
        if not img_url:
            continue
        if '?' in img_url:
            img_url = img_url.split('?')[0]
        if is_valid(img_url):
            urls.append(img_url)
    return urls

def is_valid(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def download(link_img: str, direction_name: str, count: int)-> None:
    with requests.get(link_img, stream=True) as response:
        if response.status_code != 200:
            raise Exception('Файл не найден - ошибка 200')

        file_size = int(response.headers.get('Content-Length', 0))
        first_chunk = next(response.iter_content(1024 * 10))
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(first_chunk)

        extension = dict_ext[mime_type]
        final_filename = os.path.join(direction_name)

        with open(final_filename, 'wb') as f:
            f.write(first_chunk)
            progress = tqdm.tqdm(total=file_size, init="B", init_scale=True,
                                 desc=f'Скачиваю {final_filename}')
            for chunk in response.iter_content(1024*1024):
                if chunk:
                    f.write(chunk)
                    progress.update(len(chunk))




def main(url: str, dire: str) -> None:
    for file in os.listdir(dire):
        path_file = os.path.join(dire, file)
        os.unlink(path_file)

    count = 0
    url_files = os.path.join(url)
    for url_file in url_files:
        count +=1
        download(url_file, dire, count)

if __name__ == '__main__':
    main(site_name, dir_for_images)









