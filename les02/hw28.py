# Урок 2. Циклы. Рекурсия. Функции.
# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
#

count = 0

while (1):
    try:
        user_input = int(input('Введите количество вводимых чисел = '))
        user_input_count = int(input('Введите цифру для подсчета (0-9) = '))

        for i in range(user_input):
            user_input_num = int(input(f'Введите {i + 1}-е число: '))
            while user_input_num > 0:
                if user_input_num % 10 == user_input_count:
                    count += 1
                user_input_num = user_input_num // 10

        print(f'Цифра {user_input_count} встречается {count} раз')
        break
    except:
        print('Ошибка ввода')
