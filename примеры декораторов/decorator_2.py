import time

def cache(funk):
    result = {}  # Словарь для хранения результатов
    def wrapper(a):
        if a in result:  # Если результат уже есть в кэше, возвращаем его
            return f'Значение взято из кэша: {result[a]}'
        start = time.perf_counter()  # Начинаем отсчет времени
        result[a] = funk(a)  # Вызываем функцию и сохраняем результат в словарь
        stop = time.perf_counter()  # Останавливаем отсчет времени
        return f'Значение {result[a]} получено за {stop - start} секунд'
    return wrapper


@cache
def prime_number(a):  # поиск простого числа
    data = [2, 3, 5]
    if a < len(data):
        return data[a]
    else:
        while len(data) <= a:
            pr = data[-1]
            pr += 2
            while True:
                for i in range(2, pr):  # чтобы число не делилось на 1 и на само себя
                    if pr % i == 0:
                        break  # если pr делиться хотя бы на 1 число, то цикл завершается и идет переход к следующему числу pr + 1
                else:
                    data.append(pr)
                    break
                pr += 2
        return data[a]

a_1 = prime_number(1000)
a_2 = prime_number(1000)
a_3 = prime_number(1000)
a_4 = prime_number(1000)
print(a_1)
print(a_2)
print(a_3)
print(a_4)

