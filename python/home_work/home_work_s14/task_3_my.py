class Restangle:
    """
    >>> a = Restangle(1,1)
    >>> a.get_area()
    1
    >>> a.get_perimetr()
    4
    >>> a.set_dimensions(2,2)
    >>> a.get_area()
    4
    >>> a.get_perimetr()
    8
    >>> a.set_dimensions(-1,12)
    Traceback (most recent call last):
    ...
    ValueError
    """
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        if width > 0 and height > 0 :
            self.width = width
            self.height = height
        else:
            raise ValueError

    def get_area(self):
        return self.width * self.height

    def get_perimetr(self):
        return self.width * 2 + self.height * 2


