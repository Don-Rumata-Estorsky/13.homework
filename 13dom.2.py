"""
Исключение для фуккции что прибовляет 2 к введенному числу
"""

def plus2(number):
    result = number + 2
    return result

try:
    number = float(input("Введите число: "))
    result = plus2(number)
    print("Ввод + 2 = Итого: ", result)
except ValueError:
    print("Ожидаемый тип данных — число.")
except TypeError:
    print("Ожидаемый тип данных — число.")
