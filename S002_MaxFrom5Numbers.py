# Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# Алгоритм
# 1. Ввести 5 чисел, задать тип
# 2. Обозначить первое число, как максимальное
# 3. Если следующее число больше максимального, положить в максимум это число
# 4. Повторить п.3 для всех последующих чисел
# 5. Распечатать максимальное число из введенных

# Решение 1
print(f'Введите 5 целых чисел')
num1 = int(input('Первое число: '))
num2 = int(input('Второе число: '))
num3 = int(input('Третье число: '))
num4 = int(input('Четвертое число: '))
num5 = int(input('Пятое число: '))
max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
if num4 > max_num:
    max_num = num4
if num5 > max_num:
    max_num = num5
print(f'Максимальное число = {max_num}')

# Решение 2
count_num = 5
print(f'Введите {count_num} чисел')
num = float(input('Число 1: '))
max_num = num
for i in range(count_num - 1):
    num = float(input(f'Число {i + 2}: '))
    if num > max_num:
        max_num = num
if not max_num % 1:
    print(f'Максимальное число = {round(max_num)}')
else:
    print(f'Максимальное число = {max_num}')
