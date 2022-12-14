# Вывести на экран "электронный таймер". Ставим таймер –
# часы, минуты, секунды. После отсчета срабатывает будильник.

# Алгоритм
# 1. Ввести часы, минуты и секунды
# 2. Проверить корректность ввода
# 3. Перевести все в секунды
# 4. Перебрать последовательно значения часов, минут и секунд
# 5. Когда закончится цикл с секундами, проверить оставшееся количество секунд.
# Если больше или равно 59, то присвоить новое значение секунд (59),
# затем вернуться в цикл с минутами
# 6. Повторить действия из пункта 5 для минут, заменив проверку остатка
# на больше или равно 3599, вернуться к циклу с часами
# 7. После выхода из циклов выдать сообщение о завершении

import time
hours = int(input('Введите количество часов: '))
minuts = int(input('Введите количество минут (0-59): '))
sec = int(input('Введите количество секунд (0-59): '))
total_sec = hours * 3600 + minuts * 60 + sec
if minuts > 59 or sec > 59:
    print('Некорректный ввод')
else:
    input('Нажмите Enter для старта')
    for i in range(hours, -1, -1):
        for j in range(minuts, -1, -1):
            for k in range(sec, -1, -1):
                print('{:02} : {:02} : {:02}'.format(i, j, k))
                time.sleep(1)
            total_sec -= sec + 1
            if total_sec >= 59:
                sec = 59
        if total_sec >= 3599:
            minuts = 59
    print('КУКАРЕКУУУУ!!!')
