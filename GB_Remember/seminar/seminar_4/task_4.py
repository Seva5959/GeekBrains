import os
import threading

def count_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        word_count = len(text.split(' '))
        print(f"Файл: {file_path} → {word_count} слов")

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

directory = 'nabor_sites_async'
main(directory)


















