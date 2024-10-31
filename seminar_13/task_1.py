def input_number():
    while True:
        number = input('Введите число: ')
        try:
            return int(number)
        except ValueError:
            try:
                return float(number)
            except ValueError:
                print('Нужно ввести число! ')


n = input_number()
print(n)
print(type(n))