"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
 размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def total(self):
        pass

    def coat(self):
        pass

    def costume(self):
        pass


class My_Clothers(MyAbstractClass):
    def __init__(self, my_coat, param1, my_suit, param2):
        self.param1 = param1
        self.my_coat = my_coat
        self.param2 = param2
        self.my_suit = my_suit

    @property
    def coat(self):
        print(f'расход ткани на пальто {round((self.param1 / 6.5 + 0.5), 2)}')

    @property
    def costume(self):
        print(f'расход ткани для костюма {round((2 * self.param2 + 0.3), 2)}')

    @property
    def total(self):
        print(f'расход ткани для костюма и пальто {round(((2 * self.param2 + 0.3) + (self.param1 / 6.5 + 0.5)), 2)}')


my_clother = My_Clothers('пальто', 8, 'костюм', 3)
my_clother.total
my_clother.coat
my_clother.costume
