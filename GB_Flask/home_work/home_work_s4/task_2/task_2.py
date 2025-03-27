import os
import requests
import re

# Если путь начинается с http:// или https:// → он уже готов для скачивания.
# Если путь начинается с // → добавить https:.
# Если путь начинается с / → добавить домен сайта.

src_path = "//upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/17px-Wikispecies-logo.svg.png"  # Найденный путь

txt = 'fdhgdskjghkdjg<po1 Oчень полезная информация >dsk<po1 fhdsgfjgjgsfh >fls<<po1 Мотя лох сосет горох><>>.<><><po<<>'

# 1)алгоритм по нахождению src через регулярки
# 2)загрузка всех изображений через найденные src
# 2.1)отработка 3 разных вариантов
# 3)использование мультипроцессорного способа

lst_pol = re.findall(r'<po1(.*?)>', txt)
print(lst_pol[2])






