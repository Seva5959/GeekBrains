# Неправильный код
from random import randint
from task_4 import args_deco, repeater
def game_validator(func):
    def inner(number, attempts):
        g_number = number if 0 <= number <= 100 else randint(0, 100)
        n_attempts = attempts if 0 <= attempts <= 10 else randint(0, 10)
        return func(g_number, n_attempts)

    return inner
@repeater(4)
@args_deco
@game_validator
def gusee_numbers(g_number, n_attempts):
    full_attempts = 0
    while n_attempts >= full_attempts:
        user_number = int(input(f"Введи число от 1 до 100 за {n_attempts} попыток - "))
        full_attempts +=1

        if user_number < g_number:
            print('>')
        elif user_number > g_number:
            print("<")
        else:
            print("You win")
            return  f'Вы победили. Число {g_number}, потраченно попыток {n_attempts}'
    print(f"You dalboeb {g_number}")
    return f'Вы програли. Загаданное число - {g_number}'

gusee_numbers(532, 32)

if __name__ == "__main__":
    print("start")
