import tqdm
import os
import bs4
import requests

site = ''
def get_all_src_imgs(url:str):
    urls = []
    soup = bs4.BeautifulSoup(requests.get(url).content, 'html.parser')
    for img in tqdm.tqdm(iterable=soup.find_all('img'),desc='Извлекаю тег img:'):
        img_url =






