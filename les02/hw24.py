# Урок 2. Циклы. Рекурсия. Функции.
# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

while (1):
    try:
        user_input = int(input('Введите число элементов: '))
        res = 1
        k = 1
        for i in range(1, user_input):
            res += k / (-2)
            k = k / (-2)
        print(res)
        break
    except:
        print('Ошибка ввода')