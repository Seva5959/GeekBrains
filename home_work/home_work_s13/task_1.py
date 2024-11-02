import random

NIRVANA_KARMA = 500

# Определение пользовательских исключений
class KillError(Exception):
    def __init__(self):
        super().__init__("Убийство. Вы и убили-с!")

class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство. Пьянству бой!")

class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Вы попали в аварию. Стоит следить за дорогой.")

class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Вы обожрались. Следует сократить порции.")

class DepressionError(Exception):
    def __init__(self):
        super().__init__("На вас напала хандра. Уныние - грех.")

# Функция, моделирующая один день жизни
def one_day():
    # Случайное количество кармы от 1 до 7
    day_karma = random.randint(1, 7)
    
    # Случайная вероятность выброса исключения
    if random.randint(1, 10) == 5:
        # Случайный выбор исключения
        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception
    
    return day_karma

# Основная функция симулятора
def main():
    karma = 0
    # Открываем файл для записи логов
    with open('karma.log', 'w', encoding='utf-8') as fl_logger:
        while True:
            try:
                # Прибавляем карму за один день
                karma += one_day()
            except Exception as ex:
                # Записываем информацию об исключении в файл
                fl_logger.write(f'{ex}\n')
            
            # Проверяем, достигнуто ли необходимое количество кармы
            if karma >= NIRVANA_KARMA:
                break
    
    # Сообщаем о достижении цели
    print('Вы достигли Нирваны!')
    print('Омм')

# Запуск основной функции
if __name__ == "__main__":
    main()
