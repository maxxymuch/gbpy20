# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
#

while(1):
    print('Введите номер буквы в англ алфавите от 1 до 26:')
    try:
        num = int(input())
        if (num <= 26):
            char = chr(num + 64)
            print(f'Это буква "{char}"')
            break
        else:
            print('Введенная цыфра больше 26')
    except:
        print('Ошибка формата ввода')
