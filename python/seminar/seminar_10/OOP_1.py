"""Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.

Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.

Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома: уменьшать количество
денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов данный метод принимает объект дома и его цену."""
class Human:
    default_name = "Homosapiens"
    default_age = 20
    def __init__(self,name = default_name,age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'{self.name},возраст {self.age} лет, имеет {self.__house}, {self.__money} рублей')

    @staticmethod
    def default_info():
        print(f'дефолтное имя {Human.default_name}, дефолтный возраст {Human.default_age}')

    def __make_deal(self, house, prise):
        self.__money -= prise
        self.__house = house

    def earn_money(self,amoint):
        self.__money +=amoint

    def buy_house(self ,house, sale):
        price = house.final_price(sale)
        if self.__money >= price:
            self.__make_deal(house,price)
        else:
            print(f"Иди работай бомжара. Тебе не хватает {price - self.__money} рублей ")



class House:
    count = 0
    def __init__(self,area, coast):
        self._area = area
        self._coast = coast

    def final_price(self,procent):
        end_coast = self._coast *  (100 - procent)  / 100
        print(f'Final price : {end_coast}')
        return end_coast


matbek = Human("Матвей",19)
matbek.earn_money(40_000)
hostel = House(15,1000)
barak = House(25,1_000_000)
matbek.buy_house(hostel,1)
matbek.earn_money(940_989+2)
matbek.buy_house(barak,2)
print(matbek.info())






