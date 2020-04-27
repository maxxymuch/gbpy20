# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

while (1):
    first_point = input('Введите через запятую координаты x,y первой точки : ')
    second_point = input('Введите через запятую координаты x,y второй точки: ')
    first_point = first_point.split(',')
    second_point = second_point.split(',')
    try:
        x1 = float(first_point[0])
        x2 = float(second_point[0])
        y1 = float(first_point[1])
        y2 = float(second_point[1])
        print(f'Уранение прямой вида y=kx+b: y = {(y2 - y1) / (x2 - x1)}x + {(x2 * y1 - x1 * y2) / (x2 - x1)}')
        break
    except:
        print('Неверный ввод или значения')
        continue
