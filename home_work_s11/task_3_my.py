class Rectangle:
    def __init__(self,width,height=None):
        self.width = width
        self.height = height
        if self.height is None:
            self.height = self.width
    def perimetr(self):
        return self.height * 2 + self.width * 2

    def area(self):
        return self.width*self.height

    def __add__(self, other):
        new_width = self.width + other.width
        new_heigth = self.height + other.height
        new_parametr = new_heigth * 2 + new_width * 2
        return f'Новый прямоугольник со сторонами {new_heigth}, {new_width} и пермиметром {new_parametr}'


a = Rectangle(10,23)
d = Rectangle(10)
print(a+d)
#fnjsjdf fsdfjksd fs kfsjd fs


