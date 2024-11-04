class Rectangle:
    def __init__(self,width,height=None):
        self.width = width
        self.height = height
        if self.height is None:
            self.height = self.width
    def perimeter(self):
        return f'{self.height * 2 + self.width * 2}'

    def area(self):
        return self.width*self.height

    def __add__(self, other):
        new_width = self.width + other.width
        new_heigth = self.height + other.height
        new_parametr = new_heigth * 2 + new_width * 2
        g = f'Rectangle({new_heigth}, {new_width})'
        return eval(g)

    def __sub__(self, other):
        new_width = self.width - other.width
        new_heigth = self.height - other.height
        new_parametr = new_heigth * 2 + new_width * 2
        g = f'Rectangle({new_heigth}, {new_width})'
        return eval(g)

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        else:
            return False

    def __eq__(self,other):
        if self.area() == other.area():
            return True
        return False

    def __le__(self, other):
        if self.area() <= other.area():
            return True
        return False

    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")
rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")