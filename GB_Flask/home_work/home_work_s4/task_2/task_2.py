import os
import requests



# Если путь начинается с http:// или https:// → он уже готов для скачивания.
# Если путь начинается с // → добавить https:.
# Если путь начинается с / → добавить домен сайта.

src_path = "//upload.wikimedia.org/wikipedia/commons/thumb/d/df/Wikispecies-logo.svg/17px-Wikispecies-logo.svg.png"  # Найденный путь

txt = 'fdhgdskjghkdjg<po1 Oчень полезная информация >dskfls<<>>.<><><po<<>'

# 1)алгоритм по нахождению src через регулярки
# 2)загрузка всех изображений через найденные src
# 2.1)отработка 3 разных вариантов
# 3)использование мультипроцессорного способа