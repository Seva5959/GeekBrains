import os
import re
import requests

VALID_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "svg", "webp", "bmp", "tiff"}
DIR_FOR_IMAGES = 'image_storage'
site = 'example.html'
domen = 'https://wikipedia.org'

def find_src_in_html(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        html_txt = f.read()
    src_list = re.findall(r'<img[^>]+src="([^"]+)"', html_txt)

    return src_list

def last_prf(list_src_tag):
    data = []
    for elem in list_src_tag:
        prf = elem.rsplit('.', 1)[-1].lower() if '.' in elem else ''
        if prf in VALID_EXTENSIONS:
            data.append([elem, prf])

    return data

def downloader(path_dire, src_list):
    count = 1
    for elem in src_list:
        src = elem[0]
        prf = elem[1]
        if src[0:2] == '//': # Отрабатываю если путь начинается с //
            url = 'https:' + src
        elif src[0:2] == 'ht': # Отрабатываю если путь начинается с https или http
            url = src
        else: # Отрабатываю если путь начинается с \
            url = domen + src

        responce = requests.get(url)
        if responce.status_code == 200:
            file_name = f'foto_{count}.{prf}'
            file_path = os.path.join(path_dire, file_name)
            with open(file_path, mode='wb') as f:
                f.write(responce.content)
            count += 1

def main(site_direction):
    src_lst_raw = find_src_in_html(site)
    src_list_ready = last_prf(src_lst_raw)
    downloader(DIR_FOR_IMAGES, src_list_ready)


main()
