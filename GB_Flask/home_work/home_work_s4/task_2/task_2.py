import os
import re
import requests
import time

VALID_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "svg", "webp", "bmp", "tiff"}
DIR_FOR_IMAGES = 'image_storage'
DIR_SITES = 'nabor_sites'


def return_filename_domain(direction: str) -> list:
    '''
    Функция проходит по указанной директории состоящая из html файлов.
    Возвращает список всех файлов и домены
    '''

    result = []
    for filename_html in os.listdir(direction):
        name_sites = filename_html.split('_')[1]  # Берем второй элемент 'multipocesswww', 'google', 'com.html'
        domain = 'https://' + name_sites + '.com'
        filename = os.path.join(direction, filename_html)
        result.append([filename, domain])
    return result


def find_src_in_html(filename: str) -> list[str]:
    '''
    Функция обходит html файл и возвращает список всех src относящихся к img.
    '''

    with open(filename, mode='r', encoding='utf-8') as f:
        html_txt = f.read()
    src_list = re.findall(r'<img[^>]+src="([^"]+)"', html_txt)

    return src_list


def last_prf(list_src_anf_domain: list) -> list:
    '''
    Функция находит разрешение src, например: img, jpeg, svg.
    Также возвращает список включающих 1)src, 2)само prf
    '''

    list_src_tag = list_src_anf_domain
    data = []
    for elem in list_src_tag:
        prf = elem.rsplit('.', 1)[-1].lower() if '.' in elem else ''
        if prf in VALID_EXTENSIONS:
            data.append([elem, prf])

    return data


def downloader(list_src_prf: list, main_dire: str, domain: str) -> None:
    '''
    Функция скачивает изображение в директорию, которая будет создана в указанной директории.
    '''

    count = 1
    for elem in list_src_prf:
        src = elem[0]
        prf = elem[1]
        if src[0:2] == '//':  # Отрабатываю если путь начинается с //
            url = 'https:' + src
        elif src[0:2] == 'ht':  # Отрабатываю если путь начинается с https или http
            url = src
        else:  # Отрабатываю если путь начинается с \
            url = domain + src

        response = requests.get(url)
        if response.status_code == 200:
            # re.search: получаем имя сайта от его домена
            dire_for_img = main_dire + re.search(r"/([^.]+)", domain).group(1)
            os.makedirs(dire_for_img, exist_ok=True)
            name_img = f'foto_{count}.{prf}'
            file_path = os.path.join(dire_for_img, name_img)
            with open(file_path, mode='wb') as f:
                f.write(response.content)
            count += 1


def main():
    start_time = time.time()
    for elem in return_filename_domain(DIR_SITES):
        html = elem[0]
        domain = elem[1]
        src_lst_raw = find_src_in_html(html)
        src_list_ready = last_prf(src_lst_raw)
        downloader(src_list_ready, DIR_FOR_IMAGES, domain)
    print(f'Работа кода окончена. Было затрачено {time.time()-start_time}')

main()
