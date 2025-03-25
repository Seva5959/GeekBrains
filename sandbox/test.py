import os
import requests

dir_name = 'image_storage'
file_path = os.path.join(dir_name, 'Wikipedia-logo.png')

base_url = "https://www.wikipedia.org/"
image_path = "portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png"  # Найденный путь
image_url = base_url + image_path  # Полный URL изображения

response = requests.get(image_url)  # Отправляем GET-запрос
if response.status_code == 200: # Проверяем, что запрос успешный
    with open(file_path, "wb") as file:
        file.write(response.content)  # Именно метод content позволяет записывать png, mp3, ZIP, PDF

# ----------------------------------------------------------------

import os
import requests

dir_name = 'image_storage'
file_path = os.path.join(dir_name, 'Wikipedia-logo.png')

base_url = "https:"
src_path = "//upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/17px-Wikispecies-logo.svg.png"  # Найденный путь
image_url = base_url + src_path  # Полный URL изображения

response = requests.get(image_url)  # Отправляем GET-запрос
if response.status_code == 200: # Проверяем, что запрос успешный
    with open(file_path, "wb") as file:
        file.write(response.content)  # Именно метод content позволяет записывать png, mp3, ZIP, PDF
        print('Успешно скачано')
else:
    print('Oшибка скачивания')





