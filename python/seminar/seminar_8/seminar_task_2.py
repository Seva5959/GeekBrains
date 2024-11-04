import json
def save_json():
    with open("file.json", "r", encoding="utf-8") as f:
        json_file = json.load(f)

    data_ID = set()
    while True:
        lvl = input("Введите уровень вашего доступа (1-7) - ")
        if not lvl.isdigit() or not 1 <= int(lvl) <= 7:
            print("Вы ввели некорректное значение")
            continue

        id = input("Введите ваш айди - ")
        if id in data_ID:
            print("Данное айди уже занято")
            continue
        data_ID.add(id)

        name = input("Введите ваше имя - ")

        if lvl not in json_file:
            json_file[lvl] = []

        json_file[lvl].append({"name": name, "id": id})

        with open("file.json", 'w', encoding="utf-8") as f_json:
            json.dump(json_file, f_json, ensure_ascii=False, indent=4)

save_json()