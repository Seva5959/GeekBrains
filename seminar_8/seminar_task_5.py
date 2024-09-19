from pathlib import Path
import json
import pickle


def json_to_pickle():
    current_dir = Path.cwd()
    seminar_dir = current_dir / 'seminar_8'

    json_files = list(seminar_dir.glob('*.json'))
    if not json_files:
        print(f"JSON файлы не найдены в директории {seminar_dir}")
        return

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        pickle_file = json_file.with_suffix('.pickle')
        with open(pickle_file, 'wb') as f:
            pickle.dump(data, f)

        print(f"Создан файл: {pickle_file}")


json_to_pickle()