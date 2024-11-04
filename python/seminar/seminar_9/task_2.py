from random import randint

def game_validator(func):
    def inner(number,attempts):
        g_number = number if 0 <= number <= 100 else randint(0,100)
        n_attempts = attempts if 0 <= attempts <= 10 else randint(0,10)
        return func(g_number,n_attempts)
    return inner

@game_validator
def gusee_numbers(g_number,n_attempts):

    while n_attempts > 0:
        user_number = int(input(f"Введи число от 1 до 100 за {n_attempts} попыток - "))
        n_attempts -=1
        if user_number < g_number:
            print('>')
        elif user_number > g_number:
            print("<")
        else:
            print("You win")
            return
    print(f"You dalboeb {g_number}")

gusee_numbers(532,32)
