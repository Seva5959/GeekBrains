class Circle:
    def __init__(self,radius):
        self.radius = radius

    def len_okr(self):
        return self.radius * 2 * 3.14

    def area_okr(self):
        return (self.radius ** 2) * 3.14


a = Circle(10)
print(a.len_okr())
print(a.area_okr())