# Урок 2. Циклы. Рекурсия. Функции.
# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.
#

import re

new_digit = ''

user_input = input('Введите целое натуральное число: ')

for el in user_input:
    if (el.isdigit()):
        new_digit = new_digit + el

num = re.findall(r'[0-9]', user_input)
rev = ''
for el in reversed(num):
    rev = rev + el
print(f'Обратное число: {rev}')