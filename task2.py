"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
 Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве
  делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


ch1 = input("Введите  числитель: ")
ch2 = input("Введите знаменатель: ")

try:
    if int(ch2) == 0:
        raise OwnError("На ноль делить нельзя!")
except ValueError:
    print("Это не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. {int(ch1) / int(ch2)}")