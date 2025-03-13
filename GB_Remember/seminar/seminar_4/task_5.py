import os
import multiprocessing


def count_word(file):
    with open(file, mode='r', encoding='utf-8') as f:
        text = f.read()
        count = len(text.split(' '))
        return file, count


def main(dir_path):
    list_file = [os.path.join(dir_path, i) for i in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, i))]
    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        result = pool.map(count_word, list_file)  # Нужно передавать задачи списком

    for file, count in result:
        print(f'{file} count words: {count}')


if __name__ == '__main__':  # Мультипроцессорный подход не может обойтись без этого
    main('nabor_sites_thread')  # Иначе ошибки
