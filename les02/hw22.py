# Урок 2. Циклы. Рекурсия. Функции.
# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

odd_digits = 0
even_digits = 0
user_input = input('Введите целое число: ')
for number in user_input:
    try:
        if int(number) % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
    except:
        print(f'Отброшено {number}')
print(f'В числе {user_input}: {odd_digits} нечетных и {even_digits} четных цифр')
