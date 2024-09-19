import random

TRIES = 10

# Определение производных элементов
class Storm:
    answer = "Вы сложили Воду и Воздух и получили класс Шторм"

class Steam:
    answer = "Вы сложили Воду и Огонь и получили класс Пар"

class Mud:
    answer = "Вы сложили Воду и Землю и получили класс Грязь"

class Bolt:
    answer = "Вы сложили Воздух и Огонь и получили класс Молния"

class Dust:
    answer = "Вы сложили Воздух и Землю и получили класс Пыль"

class Lava:
    answer = "Вы сложили Огонь и Землю и получили класс Лава"

# Дополнительный элемент
class Fog:
    answer = "Вы сложили Воду и Пыль и получили класс Туман"

# Определение базовых элементов
class Water:
    def __add__(self, other):
        if isinstance(other, Soil):
            return Mud()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Dust):
            return Fog()  # Взаимодействие Воды и Пыли

class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Bolt()
        elif isinstance(other, Soil):
            return Lava()

class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Bolt()
        elif isinstance(other, Soil):
            return Dust()

class Soil:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()

# Основная функция
def main():
    elements = [Water(), Fire(), Air(), Soil(), Dust()]  # Добавили элемент Пыль для взаимодействия
    try_count = 0
    while try_count < TRIES:
        element_a = random.choice(elements)
        element_b = random.choice(elements)
        result = element_a + element_b
        if result is None:
            continue
        try_count += 1
        print(result.answer)
        print()

# Запуск программы
main()
