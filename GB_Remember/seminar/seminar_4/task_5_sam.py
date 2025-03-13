import os
import multiprocessing
import time

start_time = time.time()
def cpunt_words(file):
    with open(file, mode='r', encoding='utf-8') as f:
        text = f.read()
        return file, len(text.split(' '))


def main(dir_path):
    list_files = []
    for filename in os.listdir(dir_path):
        file = os.path.join(dir_path, filename)
        if os.path.isfile(file):
            list_files.append(file)

    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        res = pool.map(cpunt_words, list_files)

    for file, count in res:
        print(file, count)

if __name__ == '__main__':
    main('nabor_sites_thread')
    print(f'\n{time.time()-start_time:.2f}')