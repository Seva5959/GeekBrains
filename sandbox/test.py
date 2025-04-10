from bs4 import BeautifulSoup
# filename = 'index.html'
#
# with open(filename, 'r') as f:
#     txt = f.read()
#
# soup = BeautifulSoup(txt, 'html.parser')
# rez = soup.find_all('body')
# print(rez)

import tqdm
import time
count= 0
numbers = [i for i in range(1, 1_000_000_000)]

for number in tqdm.tqdm(numbers, 'Обработка чисел'):
    count += 1







