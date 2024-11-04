from pathlib import Path


def rename_files(desired_name, num_digits, source_ext, target_ext):
    adress_dir = Path("test_folder").resolve()
    files = sorted(adress_dir.glob(f'*{source_ext}'))
    renamed_files = []

    for k, file in enumerate(files, start=1):
        new_digit = str(k).zfill(num_digits)
        new_name = f"{desired_name}{new_digit}.{target_ext}"
        new_name_path = file.with_name(new_name)
        file.rename(new_name_path)
        renamed_files.append(new_name)

    # Добавляем файлы, которые не были переименованы
    other_files = [f.name for f in adress_dir.glob('*') if f.name not in renamed_files]
    renamed_files.extend(other_files)

    return sorted(renamed_files)


# Использование функции
result = rename_files(desired_name="new_file_", num_digits=3, source_ext=".mp3", target_ext="..txt")
print(", ".join(result))