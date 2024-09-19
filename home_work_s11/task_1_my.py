class Matrix:
    def __init__(self,data_matrix):
        self.data_matrix = data_matrix

    def __add__(self, other):
        data_3 = []
        stroka = []
        for row in range(len(self.data_matrix)):
            for column in range(len(self.data_matrix[0])):
                stroka.append(self.data_matrix[row][column] + other.data_matrix[row][column])
            data_3.append(stroka)
            stroka = []
        return data_3

    def __sub__(self, other):
        data_3 = []
        stroka = []
        for row in range(len(self.data_matrix)):
            for column in range(len(self.data_matrix[0])):
                stroka.append(self.data_matrix[row][column] - other.data_matrix[row][column])
            data_3.append(stroka)
            stroka = []
        return data_3

    def tranc_matrix(self):
        new_matrix = []
        rows = []
        for column in range(len(self.data_matrix[0])):
            for row in self.data_matrix:
                rows.append(row[column])
            new_matrix.append(rows)
            rows = []
        return new_matrix

    def __str__(self):
        txt = ''
        for row in self.data_matrix:
            txt += str(row) + '\n'
        return f'Матрица \n{txt}'

mat_1 = [[1,1,1],
         [2,2,2],
         [3,3,3]]

mat_2 = [[4,4,5],
         [20,72,6],
         [-3,763,93]]


test_1 = Matrix(mat_1)
test_2 = Matrix(mat_2)
print(test_2+test_1)
print(test_1)