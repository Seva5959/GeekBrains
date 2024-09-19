from random import randint as rnd
def mix_name(number):
    gl_list = ['a', 'o', 'y', 'e', 'u', 'i']
    sog_list = ['b', 'c', 'd', 'f', 'g', 'h', 'p', 'r', 's', 't', 'w', 'm', 'n', 'x', 'z']

    with open("data_task_2.txt", "w", encoding="utf-8") as f:
        for i in range(number):
            name = ""  # Обнуляем переменную name для нового имени
            k = 0
            for j in range(rnd(4, 8)):  # Длина слова от 4 до 7 символов
                if k == 0:
                    name += gl_list[rnd(0, len(gl_list) - 1)]
                    k = 1
                else:
                    name += sog_list[rnd(0, len(sog_list) - 1)]
                    k = 0
            f.write(name + "\n")  # Записываем имя в файл
mix_name(5)
