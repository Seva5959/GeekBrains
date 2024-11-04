""""Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса."""

class Cat:
    def __init__(self,name,wool,visual_acuity,cute,height,fear_of_dogs = True):
        self.name = name
        self.wool = wool
        self.visual_acuity = visual_acuity
        self.fear_of_dogs = fear_of_dogs
        self.cute = cute
        self.height = height
        self.hunger = 5

    def info(self):
        return (f'Ваша кошка : {self.name},у нее {self.wool} шерсть.\n '
                f'Острота зрения {self.visual_acuity}, боязнь к собакам  {self.fear_of_dogs}. Милота = {self.cute}\n'
                f'Рост {self.name} составляет {self.height} см')

    def eat(self,quantity_of_sausage):
        if  quantity_of_sausage:
            self.hunger += quantity_of_sausage
        if self.hunger < 5:
            return (f"Животное {self.name} испытывает голод. Ему не хватает {5 - self.hunger } сосисок ")
        else:
            return (f'Животное {self.name} сыто и не хочет кушать')

class Human:
    def __init__(self,name,age,sex,height):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.hunger = 5
    def info(self):
        return f'Человека завут {self.name}, ему {self.age} лет. Пол {self.sex} Рост - {self.height}\n'

    def eat(self,quantity_of_sausage):
        if  quantity_of_sausage:
            self.hunger += quantity_of_sausage
        if self.hunger < 5:
            return (f"Животное {self.name} испытывает голод. Ему не хватает {5 - self.hunger } сосисок ")
        else:
            return (f'Животное {self.name} сыто и не хочет кушать')

class Crocodile:
    def __init__(self,length_of_the_tail,length_of_the_teeth,number_of_sheep_eaten,name,height):
        self.length_of_the_tail = length_of_the_tail
        self.length_of_the_teeth = length_of_the_teeth
        self.number_of_sheep_eaten = number_of_sheep_eaten
        self.name = name
        self.height = height
        self.hunger = 5
    def info(self):
        return  (f'Крокодила завут {self.name}. Длина его зубов {self.length_of_the_teeth} см поражает воображение \n'
                f'Длина хвоста {self.length_of_the_tail} см. Сегодня он скушал {self.number_of_sheep_eaten} овец \n'
                f'Его рост составляет {self.height} cm \n')

    def eat(self,quantity_of_sausage):
        if  quantity_of_sausage:
            self.hunger += quantity_of_sausage
        if self.hunger < 5:
            return (f"Животное {self.name} испытывает голод. Ему не хватает {5 - self.hunger } сосисок ")
        else:
            return (f'Животное {self.name} сыто и не хочет кушать')

gena = Crocodile("65","13",4,"Гена",250)
oleg = Human("Андрей","24","Т-34",180)
Miky = Cat("Мику", "длинная","+10", "зашкаливает",45,True)
print(Miky.info())
print(Miky.eat(-4))
print(oleg.info())
print(oleg.eat(2))
print(gena.info())