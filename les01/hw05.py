# Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python
# 5. По1льзователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
#

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

print('Ведите две прописные буквы латинского алфавита:')

while (1):
    l_str = input('Первая буква = ')
    if isinstance(type_check(l_str),str):
        l_str = l_str[0].upper()
        break
    else:
        print('Ввод не символьный, повторите ввод')
        continue

while (1):
    r_str = input(f'Первая буква = {l_str} Вторая буква = ')
    if isinstance(type_check(r_str),str):
        r_str = r_str[0].upper()
        break
    else:
        print('Ввод не символьный, повторите ввод')
        continue

l_pos= ord(l_str) - 64
r_pos = ord(r_str) - 64
letter_count = abs(l_pos - r_pos) - 1
print(f'Буква "{l_str}" {l_pos}-я в алфавите\n'
      f'Буква "{r_str}" {r_pos}-я в алфавите\n'
      f'Между буквами {letter_count} букв')