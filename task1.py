"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
 (двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in self.matrix:
            print('')
            for j in i:
                print(j, end=" ")

    def __add__(self, other):
        self.result = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]
        for ind, i in enumerate(self.matrix):
            for ind1, j in enumerate(i):
                self.result[ind][ind1] = (self.matrix[ind][ind1] + other.matrix[ind][ind1])

        for i in self.result:
            print('')
            for j in i:
                print(j, end=" ")
        return self.result


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
m1.__str__()
print('\n', 30 * "-")
m2.__str__()
print('\n', 30 * "-")
m1 + m2
