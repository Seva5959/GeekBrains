import requests
import magic

dict_ext = {'image/jpeg':'jpeg',
            'image/png':'png',
            'image/gif':'gif',
            'image/webp':'webp',
            'image/svg+xml':'svg+',}
url_img = 'https://example.com/file'
# Отправляем GEТ-запрос, stream=True указывает, что хоти скачать не весь файл
with requests.get(url_img, stream=True) as r:
    # Читаем первые 2 КБ
    chunk = next(r.iter_content(2048))
# Идет проверка типа
mime = magic.from_buffer(chunk, mime=True)
if str(mime) in dict_ext:
    ext = dict_ext[mime]
else:
    return

# image / jpeg – JPEG
#
# image / png – PNG
#
# image / gif – GIF
#
# image / svg + xml – SVG
#
# image / webp – WebP
