class Rectangle:
    def __init__(self, width, height=None):
        # Если высота не указана, устанавливаем ее равной ширине (создаем квадрат)
        self.width = width
        self.height = height if height is not None else width

    # Метод для вычисления периметра прямоугольника
    def perimeter(self):
        return 2 * (self.width + self.height)

    # Метод для вычисления площади прямоугольника
    def area(self):
        return self.width * self.height

    # Магический метод для сложения двух прямоугольников
    def __add__(self, other):
        # Сложение периметров
        new_perimeter = self.perimeter() + other.perimeter()
        # Обратный расчет сторон для нового прямоугольника
        new_width = new_perimeter // 4
        new_height = new_width
        return Rectangle(new_width, new_height)

    # Магический метод для вычитания одного прямоугольника из другого
    def __sub__(self, other):
        # Вычитание периметров
        new_perimeter = abs(self.perimeter() - other.perimeter())
        # Обратный расчет сторон для нового прямоугольника
        new_width = new_perimeter // 4
        new_height = new_width
        return Rectangle(new_width, new_height)

    # Метод сравнения по площади (меньше)
    def __lt__(self, other):
        return self.area() < other.area()

    # Метод сравнения на равенство по площади
    def __eq__(self, other):
        return self.area() == other.area()

    # Метод сравнения по площади (меньше или равно)
    def __le__(self, other):
        return self.area() <= other.area()

    # Строковое представление прямоугольника для пользователя
    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    # Строковое представление прямоугольника для разработчика
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


# Примеры работы с классом Rectangle
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

# Вывод периметра и площади
print(f"Периметр rect1: {rect1.perimeter()}")  # Вывод: 30
print(f"Площадь rect2: {rect2.area()}")        # Вывод: 21

# Сравнение прямоугольников по площади
print(f"rect1 < rect2: {rect1 < rect2}")       # Вывод: False
print(f"rect1 == rect2: {rect1 == rect2}")     # Вывод: False
print(f"rect1 <= rect2: {rect1 <= rect2}")     # Вывод: False

# Сложение и вычитание прямоугольников
rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")  # Вывод: 50
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")          # Вывод: 2

# Дополнительный тест для repr и str
print(rect3)                                   # Вывод: Прямоугольник со сторонами 12 и 12
print(repr(rect4))                             # Вывод: Rectangle(2, 2)
