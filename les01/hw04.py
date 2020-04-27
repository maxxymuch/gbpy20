# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 4. Написать программу, которая генерирует в указанных пользователем границах:
# - случайное целое число;
# - случайное вещественное число;
# - случайный символ.
# - Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
#

import random


def type_check(*args):
    try:
        exp_type = int(args[0])
        return exp_type
    except:
        try:
            exp_type = float(args[0])
            return exp_type
        except:
            return args[0]

# --------------------------------int----------------------------------------

print('Ведите границы для случайного целого числа:')
while (1):
    l_int = input('Левая граница = ')
    if isinstance(type_check(l_int),int):
        l_int = int(l_int)
        break
    else:
        print('Число не целое, повторите ввод')
        continue

while (1):
    r_int = input(f'Левая граница = {l_int} Правая граница = ')
    if isinstance(type_check(r_int),int):
        r_int = int(r_int)
        break
    else:
        print('Число не целое, повторите ввод')
        continue

# --------------------------------float----------------------------------------

print('Ведите границы для случайного вещественного числа:')

while (1):
    l_float = input('Левая граница = ')
    if isinstance(type_check(l_float),float):
        l_float = float(l_float)
        break
    else:
        print('Число не вещественное, повторите ввод')
        continue

while (1):
    r_float = input(f'Левая граница = {l_float} Правая граница = ')
    if isinstance(type_check(r_float),float):
        r_float = float(r_float)
        break
    else:
        print('Число не вещественное, повторите ввод')
        continue

print('Ведите границы для случайной буквы:')

while (1):
    l_str = input('Левая граница = ')
    if isinstance(type_check(l_str),str):
        l_str = l_str[0].upper()
        break
    else:
        print('Ввод не символьный, повторите ввод')
        continue

while (1):
    r_str = input(f'Левая граница = {l_str} Правая граница = ')
    if isinstance(type_check(r_str),str):
        r_str = r_str[0].upper()
        break
    else:
        print('Ввод не символьный, повторите ввод')
        continue

res_int = random.randint(l_int, r_int)
res_float = random.uniform(l_float, r_float)
res_char = chr(random.randint(ord(l_str), ord(r_str)))

print(f'Случайное целое число: {res_int}\n'
      f'Случайное вещественное число: {res_float}\n'
      f'Случайная буква: "{res_char}"')
