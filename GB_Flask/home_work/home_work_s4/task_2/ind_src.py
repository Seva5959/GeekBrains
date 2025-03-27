import os
import re

VALID_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "svg", "webp", "bmp", "tiff"}
def find_src_in_html(file_name):
    with open(file_name, mode='r', encoding='utf-8') as f:
        html_txt = f.read()
    src_list = re.findall(r'<img[^>]+src="([^"]+)"', html_txt)

    return src_list



rez = find_src_in_html('example.html')

def last_prf(list_src_tag):
    data = {}
    for elem in list_src_tag:
        prf = elem.rsplit('.', 1)[-1].lower() if '.' in elem else ''
        if prf in VALID_EXTENSIONS:
            if prf not in data:
                data[prf] = 1
            else:
                num = data[prf]
                data[prf] = int(num) + 1

    return data

print(last_prf(rez))

