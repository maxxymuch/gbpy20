# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

################################## Вариант 1 #########################################
while (1):
    try:
        user_input = int(input('Введите трехзначное число: '))
        user_input = str(user_input)
        if len(user_input) == 3:
            break
        else:
            print('Вы ввели отличное число символов от 3')
    except:
        print('Ошибка формата ввода')


print(f'Суммм цифр числа {user_input}: {int(user_input[0]) + int(user_input[1]) + int(user_input[2])}')
print(f'Произведение цифр {user_input}: {int(user_input[0]) * int(user_input[1]) * int(user_input[2])}')
print(f'\n')

################################## Вариант 2 #########################################

while (1):
    try:
        x = int(input('Введите трехзначное число: '))
        num1 = x % 10
        x = x // 10
        num2 = x % 10
        num3 = x // 10
        num4 = num3 % 10
        if (num1 != 0 and num2 != 0 and num3 != 0 and num4 == num3):
            break
        else:
            print('Вы ввели отличное число символов от 3')
    except:
        print('Ошибка формата ввода')

print(f'Сумма: {num1 + num2 + num3}, '
      f'\nПроизведение: {num1 * num2 * num3}')
print(f'\n')

################################## Вариант 3 #########################################

while (1):
    try:
        user_input = int(input('Введите трехзначное число: '))
        user_input = str(user_input)
        if len(user_input) == 3:
            break
        else:
            print('Вы ввели отличное число символов от 3. Лишние символы отбрасываются')
            user_input = (user_input[0:3])
            break
    except:
        print('Ошибка формата ввода')


print(f'Суммм цифр числа {user_input}: {int(user_input[0]) + int(user_input[1]) + int(user_input[2])}')
print(f'Произведение цифр {user_input}: {int(user_input[0]) * int(user_input[1]) * int(user_input[2])}')