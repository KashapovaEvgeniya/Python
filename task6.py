"""
 Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
  В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
  В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
  вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
  только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
  соответственно. В методе деления должно осуществляться округление значения до целого числа.
"""

class Cell:
    def __init__(self, param):
        self.param =param

    def __str__(self):
        return f"{self.param}"

    def __add__(self, other):
        return Cell(self.param + other.param)

    def __sub__(self, other):
        return self.param - other.param

    def __mul__(self, other):
        return self.param * other.param

    def __truediv__(self, other):
        if self.param > other.param:
            return round(self.param / other.param)
        else:
            print('разность двух клеток меньше 0')

    def make_order(self, number):
        result1 = self.param // number
        result2 = self.param % number
        i = 0
        while i < result1:
            print('*'* number)
            i += 1
        print('*' * result2)


my_cell = Cell(18)
my_cell2 = Cell(5)
print(my_cell + my_cell2)
print(my_cell - my_cell2)
print(my_cell * my_cell2)
print(my_cell / my_cell2)
my_cell.make_order(5)