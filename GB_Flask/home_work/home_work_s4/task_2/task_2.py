import os
import re
import time
import aiofiles
import aiohttp
import asyncio

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


async def find_src_in_html_async(filename: str) -> list[str]:
    '''
    Функция асинхронно обходит html файл и возвращает список всех src относящихся к img.
    '''

    async with aiofiles.open(filename, mode='r', encoding='utf-8') as f:
        html_txt = await f.read()
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


async def downloader(session: aiohttp.ClientSession, src: str,
                     prf: str, main_dire: str, domain: str, count: int) -> None:
    '''
    Функция скачивает изображение в директорию, которая будет создана в указанной директории.
    '''

    if src.startswith('//'):  # Отрабатываю если путь начинается с //
        url = 'https:' + src
    elif src.startswith('ht'):  # Отрабатываю если путь начинается с https или http
        url = src
    else:  # Отрабатываю если путь начинается с \
        url = domain + src

    print(f"Попытка скачивания с URL: {url}")
    async with session.get(url) as response:
        if response.status == 200:
            # re.search: получаем имя сайта от его домена
            dire_for_img = main_dire + re.search(r"/([^.]+)", domain).group(1)
            os.makedirs(dire_for_img, exist_ok=True)
            name_img = f'foto_{count}.{prf}'
            file_path = os.path.join(dire_for_img, name_img)

            async with aiofiles.open(file_path, mode="wb") as f:
               await f.write(await response.read())


async def downloader_async(list_src_prf: list, main_dire: str, domain: str):
    '''Данная функция напрямую связана с downloader.
    Чтобы использовать downloader асинхронно необходим вот такой посредник'''
    async with aiohttp.ClientSession() as session:
        # Это list comprehension (генератор списка), а не список с 2 объектами
        tasks = [
            downloader(session, elem[0], elem[1], main_dire, domain, count)
            for count, elem in enumerate(list_src_prf, start=1)
        ]
        await asyncio.gather(*tasks)


async def main():
    start_time = time.time()
    for elem in return_filename_domain(DIR_SITES):
        html = elem[0]
        domain = elem[1]
        src_lst_raw = await find_src_in_html_async(html)
        src_list_ready = last_prf(src_lst_raw)
        await downloader_async(src_list_ready, DIR_FOR_IMAGES, domain)
    print(f'Работа кода окончена. Было затрачено {time.time()-start_time}')


asyncio.run(main())
