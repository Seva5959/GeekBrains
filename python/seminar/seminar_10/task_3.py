"""Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст."""

class Human:
    def __init__(self,name,surenamem,patronymik,age):
        self.name = name
        self.surename = surenamem
        self.patronymik = patronymik
        self._age = age

    def birthday(self):
        self._age += 1
        return self._age

    def full_name(self):
        print(f'Имя : {self.name}, Фамилия : {self.surename}, Отчество : {self.patronymik}')


oleg = Human("Oleg",'ivanov','ivanuch',19)
