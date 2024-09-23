from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radiys):
        self.radiys = radiys

    def area(self):
        return self.radiys * 3.14 ** 2


h = Circle(21)
print(h.area())

