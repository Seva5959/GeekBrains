import os
import threading

def count_words(file_path):
    with open(file_path, mode='r', encoding='utf-8')as f:
        text = f.read()
        count = len(text.split(' '))
        print(f'{file_path} имеет {count} слов')



def main(dir):
    threads = []

    for file_name in os.listdir(dir):
        file_path = os.path.join(dir,file_name)

        if os.path.isfile(file_path):
            thread = threading.Thread(target=count_words, args=(file_path,))
            threads.append(thread)
            thread.start()

    for thr in threads:
        thr.join()

dir = 'nabor_sites_thread'
main(dir)












