import os
import threading
import queue

# print_lock = threading.Lock()
q = queue.Queue()
def count_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        word_count = len(text.split(' '))
    q.put((file_path, word_count)) # Лучше распологать на уровень меньше:
                                   # Для читаемости и логики

        # with print_lock: # Блокирует принт, пока 1 поток не выведет информацию.
        #     print(f'{file} count words: {count}') # Благодаря этому не будет каши

def main(directory):
    threads = []
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path): # проверяем, что не папка
            thread = threading.Thread(target=count_word, args=(file_path,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    while not q.empty():
        file, count = q.get()
        print(f'{file} count words: {count}')

directory = 'nabor_sites_thread'
main(directory)


















