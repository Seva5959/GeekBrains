import time

def blocking():
    print(f'Вы израсходовали все ваши попытки. Повторить вход можно через 5 минут\n')
    start_time = time.time()
    duration = 5 * 60
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = duration - elapsed_time

        if remaining_time <= 0:
            print("Вы израсходовали все ваши попытки. Повторить вход можно через 5 минут\n")
            break

            # Запрашиваем у пользователя время
        user_input = input("Напишите 'Time', чтобы узнать сколько осталось ждать - ")
        if user_input == "Time":
            minutes_left = remaining_time // 60
            seconds_left = remaining_time % 60
            print(f'Осталось {int(minutes_left)} минут и {int(seconds_left)} секунд')
        else:
            print("Ошибка!")


blocking()