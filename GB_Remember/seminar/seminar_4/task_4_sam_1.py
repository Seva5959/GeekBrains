import os
import threading
import queue

# print_lock = threading.Lock()
q = queue.Queue()
def count_word(file):

    with open(file, mode='r', encoding='utf-8') as f:
        text = f.read()
        count = len(text.split(' '))

        # with print_lock: # Блокирует принт, пока 1 поток не выведет информацию.
        #     print(f'{file} count words: {count}') # Благодаря этому не будет каши
    q.put((file, count))

def main(dire):
    threads = []
    for filename in os.listdir(dire):
        file_path = os.path.join(dire, filename)

        if os.path.isfile(file_path):
            thread = threading.Thread(target=count_word, args=(file_path,))
            threads.append(thread)
            thread.start()

    for thr in threads:
        thr.join()

    while not q.empty(): # Позволяет более записывать информацию с потоков в удобном
                         # для использования виде
        file, count = q.get()
        print(f'{file} count words: {count}')


dire = 'nabor_sites_thread'
print(main(dire))

