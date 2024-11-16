import re
from random import choice

FILE_NAME = 'Sapogi_Chehov.txt'
def open_txt(file_name: str) -> str:
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

print(open_txt(FILE_NAME))

pattern = r'\b[а-яА-Я]{2,}\b'

# res = re.findall(pattern, text)
# print(choice(res))
