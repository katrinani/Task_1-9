"""
Задание 2 : Вычислите значение следующего выражения (аргументы - целые
числа и вводятся с клавиатуры).Округлите результат до 3-х знаков после запятой, используя
функцию round().
"""

# блок объявления перемннных
x = int(input('Введите целое число x: '))
y = int(input('Введите целое число y: '))
z = int(input('Введите целое число z: '))

# вычисление функции
f = ((x**5 + 7) / (abs(-6) * y))**(1/3) / (7 - z % y)
print(round(f, 3))
