# Напишите программу, которая будет на вход принимать число N
# и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
#
# Алгоритм
# 1. Ввести целое число
# 2. Получить обратное число
# 3. Если введено отрицательное число, поменять значения местами
# 4. Перебрать все числа от -N до N включительно
# 5. Каждое число вывести в консоль (определенное количество значений в строке)

num = int(input('Введите целое число: '))
num_negative = - num
if num_negative > num:
    num, num_negative = num_negative, num
max_count_numbers = int(input('Укажите максимальное количество чисел в одной строке: '))
i = 0
print(f'Числа от {num_negative} до {num}: ')
while num_negative < num:
    if i < max_count_numbers:
        print(num_negative, end=', ')
    else:
        print(f'{num_negative}, ')
        i = -1
    num_negative += 1
    i += 1
print(num_negative)

