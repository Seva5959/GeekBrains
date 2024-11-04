# Класс Matrix для работы с матрицами
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Инициализация матрицы нулями
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    # Метод для сложения двух матриц
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц не совпадают для сложения")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    # Метод для вычитания двух матриц
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц не совпадают для вычитания")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    # Метод для умножения двух матриц
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    # Метод для транспонирования матрицы
    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

    # Метод для красивого вывода матрицы на экран
    def __str__(self):
        # Форматирование строк матрицы
        res = "\n".join(["\t".join(map(str, row)) for row in self.data])
        return res


# Примеры работы с классом:
# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
