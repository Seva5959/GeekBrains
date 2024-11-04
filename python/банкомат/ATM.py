from random import randrange
import csv
from pathlib import Path
from datetime import datetime
import time


def cheak_FIO(massiv):
    if len(massiv) != 3:
        return True  # возвращает  True  если фио > 3 элементов
    for data in massiv:
        for i in data:
            if i.isdigit():
                return True  # возвращает  True  если есть цифры
    return False


def tab_4_num(num):
    count = 0
    data = ''
    for i in str(num):
        count += 1
        data += i
        if count % 4 == 0:
            data += ' '
    return data


def cheak_number(massiv):
    list = []
    for data in massiv:
        for i in data:
            if not i.isdigit():
                return True  # возвращает  True  если  есть буквы
            list.append(i)
    if len(list) != 10:
        return True  # возвращает  True  если номер имеет длину отличную от 10
    return False


def cheak_email(email):  # очень условная проверка
    if len(email) < 13:
        return True
    elif "@" not in email or "." not in email:
        return True
    return False


def start_to_csv(file_name):  # создает csv файл и записывает в него шапку
    current_directory = Path()
    data = []
    files = [f for f in current_directory.iterdir()]
    for file in files:
        data.append(file.name)
    if not file_name in data:
        hedears = ["name", "surename", 'patronymik', 'telephone', 'email', 'password', "number cart", 'CVC2',
                   'pin code']
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(hedears)


def write_to_csv(file_name, name, surename, patronymik, telephone, email, password, number_cart, CVC2, pin_code):
    start_to_csv(file_name)  # Если файла нет , то мы создаем его
    with open(file_name, 'a', encoding="utf-8") as f:
        data = [name, surename, patronymik, telephone, email, password, number_cart, CVC2, pin_code, ]
        wr = csv.writer(f)
        wr.writerow(data)


def time_of_day(name, patronymik):
    full_time = datetime.now()
    hours = int(full_time.strftime("%H"))
    if 0 <= hours <= 5:
        adjective = "Доброй"
        time = 'ночи'
    elif 6 <= hours <= 11:
        adjective = "Доброе"
        time = "утро"
    elif 12 <= hours <= 15:
        adjective = "Добрый"
        time = "день"
    else:
        adjective = "Добрый"
        time = "вечер"
    return f'{adjective} {time}, {name} {patronymik}!'


def find_email_password_in_csv(file_name, email, password):
    with open(file_name, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 6:  # Есть пустые строки, поэтому нужна такая проверка
                if email == row[4] and password == row[5]:
                    return False
    return True


class ATM:
    def __init__(self):
        self.bank_name = "ATM"
        self.data = []
        self.file_name = "information_about_user.csv"

    def registration(self):
        user_name = input(f'Добро пожаловать в банк {self.bank_name} ! \nУкажите ваше ФИО  - ').split()
        while cheak_FIO(user_name):
            print("Ошибка!")
            user_name = input("Введите ваше ФИО - ").split()
        self.name = user_name[1]
        self.surename = user_name[0]
        self.patronymik = user_name[2]

        user_telephone = input("Введите ваш номер телефона : +7 ").split()
        while cheak_number(user_telephone):
            print("Ошибка!")
            user_telephone = input("Введите ваш номер телефона : +7 ").split()
        lam_f = lambda suf, data: suf + ''.join(
            item for row in data for item in row)  # превращаю user_telephone список в строку
        self.telephone = lam_f('+7', user_telephone)

        user_email = input("Введите вашу почту - ")
        while cheak_email(user_email):
            print("Ошибка")
            user_email = input("Введите вашу почту - ")
        self.email = user_email

        user_password_1 = input("Введите ваш пороль - ")  # Не буду создавать проверку, ибо при тестировке я с ума сойду
        user_password_2 = input("Подтвердите ваш пороль - ")
        while user_password_2 != user_password_1:
            user_password_2 = input("Пороли не совпадают! Введите повторно - ")
        self.password = user_password_2

        print(f'\n\t\t Процесс создания карты на  {self.name}a {self.patronymik}a')
        self.create_bank_account()

    def create_bank_account(self):
        self.num_cart = ''.join(map(str, [randrange(0, 9) for i in range(16)]))
        while self.num_cart in self.data:  # Проверяю номер карты на уникальность
            self.num_cart = ''.join(map(str, [randrange(0, 9) for i in range(16)]))
        self.data.append(self.num_cart)

        self.CVC2 = ''.join(map(str, [randrange(0, 9) for i in range(3)]))
        while self.CVC2 in self.data:  # Проверяю CVC2 на уникальность
            self.CVC2 = ''.join(map(str, [randrange(0, 9) for i in range(3)]))
        self.data.append(self.CVC2)
        self.pin_code = int(input("Создайте пин код - "))  # надо написать код для исключений
        print(f'Карта успешно создана! \n\nНомер карты: {tab_4_num(self.num_cart)} \nКод CVC2: {self.CVC2} '
              f'\nПин код: {self.pin_code}')
        # Записываем всю информацию про пользователя
        write_to_csv(self.file_name, self.name, self.surename, self.patronymik, self.telephone,
                     self.email, self.password, self.num_cart, self.CVC2, self.pin_code)

    def login(self):
        user_email = input("Для входа укажите вашу почту - ")
        user_password = input("Ваш пороль - ")
        attempt = 0
        max_attempt = 3
        while find_email_password_in_csv(self.file_name, user_email, user_password):
            print(f'Ошибка в email или в пароле! У вас осталось {max_attempt - attempt} попытки\n')
            user_email = input("Для входа укажите вашу почту - ")
            user_password = input("Ваш пороль - ")
            attempt += 1
            if attempt == max_attempt:
                print("Ваши попытки закончились")
                self.blocking()
        print("Вы успешно вошли")

    def interface(self):
        user_input = input("1)Зарегистрироваться \n2)Войти \nВыберите нужную команду - ")
        if user_input == '1':
            self.registration()
        if user_input == '2':
            self.login()

    def blocking(self):
        print(f'Вы израсходовали все ваши попытки. Повторить вход можно через 5 минут\n')
        start_time = time.time()
        duration = 5 * 60
        while True:
            elapsed_time = time.time() - start_time
            remaining_time = duration - elapsed_time
            if remaining_time <= 0:
                print("Вы израсходовали все ваши попытки. Повторить вход можно через 5 минут\n")
                break
            user_input = input("Напишите 'Time', чтобы узнать сколько осталось ждать - ")
            if user_input == "Time":
                minutes_left = remaining_time // 60
                seconds_left = remaining_time % 60
                print(f'Осталось {int(minutes_left)} минут и {int(seconds_left)} секунд')
            else:
                print("Ошибка!")
        self.interface()


# a = ATM("Всеволод","Ганник", "Алексеевич","+7 952 471 89 91",9321)
a = ATM()
a.interface()
