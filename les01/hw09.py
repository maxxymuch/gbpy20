# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
#

while (1):
    user_input = input('Введите три разных числа через запятую: ')
    user_input = user_input.split(',')
    try:
        a = float(user_input[0])
        b = float(user_input[1])
        c = float(user_input[2])
    except:
        print('Ошибка формата ввода')
    if (a == b or a == c or b == c):
        print('Одна или несколько пар чисел одинаковая. Повторите ввод')
        continue
    else:
        mid = a + b + c - max(a, b, c) - min(a, b, c)
        print(f'Число {mid} - среднее')
        break
