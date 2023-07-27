# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения
class Matrix:

    def __init__(self, matrix: list[list]):
        self.matrix = matrix

    def __str__(self):
        """Вывод на печать."""
        return self.matrix

    def __eq__(self, other):
        '''Сравнение матриц.'''
        return self.matrix == other.matrix

    def __add__(self, other):
        '''Сложение матриц. '''
        summa = []
        row = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            summa.append(row)
            row = []
        return summa


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
matrix3 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(matrix1.__str__.__doc__)
print(matrix1.__str__())
print(matrix2.__str__())
print(matrix1.__eq__.__doc__)
print(matrix1 == matrix2)
print(matrix3 == matrix2)
print(matrix1.__add__.__doc__)
print(Matrix.__add__(matrix1, matrix2))
print(Matrix.__add__(matrix3, matrix2))
