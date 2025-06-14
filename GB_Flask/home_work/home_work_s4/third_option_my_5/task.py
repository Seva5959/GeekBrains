import urllib.parse
import tqdm
import os
import bs4
import requests
import magic


name_sitec = 'https://market.yandex.ru/catalog--radiodetali-i-elektronnye-komponenty/61856/list?utm_source=yandex&utm_medium=search&utm_campaign=ymp_dp_cehac_catalog_2_adv_dyb_search_rus&utm_content=cid%3A113507160%7Cgid%3A5479839618%7Caid%3A16405798637%7Cph%3A53075288949%7Cpt%3Apremium%7Cpn%3A1%7Csrc%3Anone%7Cst%3Asearch%7Crid%3A53075288949%7Ccgcid%3A0&clid=1601&yclid=5844811900972695551&text=esp32'
dict_ext = {'image/jpeg': '.jpeg',
            'image/png': '.png',
            'image/gif': '.gif',
            'image/webp': '.webp',
            'image/svg': '.svg', }
direction = 'storage'


def get_all_src(link: str) -> list[str]:
    urls = []
    soup = bs4.BeautifulSoup(requests.get(link).content, 'html.parser')
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
        if response.status_code != 200:
            print(f'file with this url: {link} was not found! Skip it')
            return

        file_size = int(response.headers.get("Content-Length", 0))
        first_chunk = next(response.iter_content(1024*10))
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(first_chunk)
        if mime_type not in dict_ext:
            print(f"file with this type: {mime_type} unsupported! Skip it")
            return

        extension = dict_ext[mime_type]
        full_name_sitec = os.path.join(direction_to_save, f'file_{count}{extension}')

        with open(full_name_sitec, mode='wb') as f :
            f.write(first_chunk)
            progress = tqdm.tqdm(total=file_size, unit='B', unit_scale=True,
                                 desc=f'Download {full_name_sitec}')
            for chunk in response.iter_content(1024*10):
                if chunk:
                    f.write(chunk)
                    progress.update(len(chunk))


def main(link: str, direction_to_save: str) -> None:
    os.makedirs(direction_to_save, exist_ok=True)
    for file in os.listdir(direction_to_save):
        path_file = os.path.join(direction_to_save, file)
        os.unlink(path_file)

    count = 0
    url_files = get_all_src(link)
    for url_file in url_files:
        count += 1
        downloader_img(url_file, direction_to_save, count)


if __name__ == '__main__':
    main(name_sitec, direction)









