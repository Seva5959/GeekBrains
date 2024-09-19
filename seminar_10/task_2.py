class Rectangle:
    def __init__(self,width, length = None):
        self.width = width
        self.length = length if length else width

    def per(self):
        return (self.width + self.length) * 2

    def area(self):
        return self.width * self.length

