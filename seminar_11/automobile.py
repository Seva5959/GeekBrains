'''Создай базовый класс Car (Автомобиль), который будет содержать общие атрибуты:

brand (марка)
speed (максимальная скорость)
price (стоимость)
Сделай атрибуты приватными и предоставь геттеры и сеттеры для управления доступом к этим данным.

2. Наследование:
Создай классы SportsCar (Спорткар), SUV (Внедорожник) и ElectricCar (Электромобиль), которые наследуются от Car. Добавь уникальные атрибуты и методы для каждого класса:

Для SportsCar — метод для ускорения.
Для SUV — метод для прохождения бездорожья.
Для ElectricCar — метод для расчета запаса хода на одном заряде.'''

class Car:
    def __init__(self,brand,speed,price,fuel):
        self.__brand = brand
        self.__speed = speed
        self.__price = price
        self.__fuel = fuel

class SportCar(Car):
    def __init__(self,brand,speed,price,energy_resrve,turbo):
        super().__init__(brand,speed,price)
        self.__energy_reserve = energy_resrve
        self.__turbo = turbo

    def activate_turbo(self):
        if self.__turbo:
            self.__speed *= 1.2

    def deactive_turbo(self):
        if self.__turbo:
            self.__turbo = True

class Cuv(Car): # Внедорожник
    def __init__(self,brand,speed,price,fuel):
        



























































