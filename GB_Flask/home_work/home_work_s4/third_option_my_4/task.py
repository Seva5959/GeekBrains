import os
import requests
import tqdm
import bs4
import urllib.parse
import magic

name_sitec = ''
direction_save_img = ''
dict_ext = {'image/jpeg': '.jpeg',
            'image/png': '.png',
            'image/gif': '.gif',
            'image/webp': '.webp',
            'image/svg': '.svg', }

def get_all_images(link: str) -> list[str]:
    soup = bs4.BeautifulSoup(requests.get(link).content, 'html.HYI')
    urls = []
    for img in tqdm.tqdm(iterable=soup.find_all('img'), desc='Извлечение изображений'):
        img_link = img.attrs.get('src')
        if not img_link:
            continue
        img_link = urllib.parse.urljoin(link, img_link)
        if '?' in img_link:
            img_link = img_link.split('?')[0]
        if is_valid(img_link):
            urls.append(img_link)
    return urls

def is_valid(link: str) -> bool:
    parsed = urllib.parse.urlparse(link)
    return bool(parsed.scheme) and bool(parsed.netloc)

def downloader(url_img: str, name_dir: str, count: int) -> None:
    os.makedirs(name_dir, exist_ok=True)
    with requests.get(url_img, stream=True) as response:
        if response.status_code != 200:
            raise Exception("ошибка 200")

        file_size = int(response.headers.get('Content-Length', 0))
        first_chunk = next(response.iter_content(1024*10))

        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(first_chunk)

        if mime_type not in dict_ext:
            print(f"Пропускаем файл с типом {mime_type}, не поддерживаемый.")
            return

        extension = dict_ext[mime_type]
        final_filename = os.path.join(name_dir, f'foto_{count}{extension}')

        with open(final_filename, 'wb') as f:
            f.write(first_chunk)
            progress = tqdm.tqdm(total=file_size, unit="B", unit_scale=True,
                                desc=f"Скачиваю {final_filename}")
            for chunk in response.iter_content(1024*1024):
                if chunk:
                    f.write(chunk)
                    progress.update(len(chunk))


def main(url: str, dire: str) -> None:
    for file in os.listdir(dire):
        path_file = os.path.join(dire, file)
        os.unlink(path_file)

    count = 0
    url_files = get_all_images(url)
    for url_file in url_files:
        count+=1
        downloader(url_file, dire, count)


if __name__ == "__main__":
    main(name_sitec, direction_save_img)
























