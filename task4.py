"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
 В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
  параметры, уникальные для каждого типа оргтехники.
  Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.

"""


class Office:
    def __init__(self, name, price, year):
        self.name = name
        self.make = price
        self.year = year


class OfficeEquipment:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year
        self.sklad = []

    def vvod(self):
        try:
            unit = input(f'Введите модель ')
            unit_p = int(input(f'Введите цену за еденицу '))
            unit_q = int(input(f'Введите год '))
            unique = {'модель': unit, 'Цена за ед': unit_p, 'год': unit_q}
            self.sklad.append(unique)
            print(f'Текущий список -\n {self.sklad}')
        except:
            return f'Ошибка ввода данных'

        q = input(f'Для выхода - Q, продолжение - Enter')
        if q == 'Q' or q == 'q':
            print(f'Весь склад -\n {self.sklad}')

            return f'Выход'
        else:
            return OfficeEquipment.vvod(self)


class Printer(OfficeEquipment):
    def __init__(self, name, price, year):
        super().__init__(name, price, year)

    def start(self):
        print('Принтер ')


class Scanner(OfficeEquipment):
    def __init__(self, name, price, year):
        super().__init__(name, price, year)

    def start(self):
        print('Сканер')


class Xerox(OfficeEquipment):
    def __init__(self, name, price, year):
        super().__init__(name, price, year)

    def start(self):
        print('Ксерокс')


unit_1 = Printer('hp', 2000, 5)
unit_2 = Scanner('Canon', 1200, 5)
unit_3 = Xerox('Xerox', 1500, 1)
unit_1.vvod()
unit_2.vvod()
unit_3.vvod()
unit_1.start()
