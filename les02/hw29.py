# Урок 2. Циклы. Рекурсия. Функции.
# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
#

max_num = 0
max_sum = 0

while (1):
    try:
        user_input = int(input('Введите натуральное число (выход - 0): '))
        if (user_input != 0):
            number = user_input
            digits_sum = 0
            while number != 0:
                digits_sum += number % 10
                number = number // 10
            if digits_sum > max_sum:
                max_sum = digits_sum
                max_num = user_input
        else:
            break
    except:
        print('Ошибка ввода')
print(f'Сумма цифр = {max_sum} числа {max_num}')