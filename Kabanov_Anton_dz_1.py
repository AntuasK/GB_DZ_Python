# Задание 1 (Конвертация времени)

def convert_time(duration):
    time_1 = []
    # Сколько суток
    calculate = int(duration // 86400)
    time_1.append(calculate)
    if calculate > 0:
        duration = duration - 86400 * calculate

    # Сколько часов
    calculate = int(duration // 3600)
    time_1.append(calculate)
    if calculate > 0:
        duration = duration - 3600 * calculate

    # Сколько минут
    calculate = int(duration // 60)
    time_1.append(calculate)
    if calculate > 0:
        duration = duration - 60 * calculate

    # остаток в секундах
    time_1.append(duration)

    # фиксируем время
    day = time_1[0]
    hours = time_1[1]
    minute = time_1[2]
    sec = time_1[3]
    # Можно использовать индексы в конструкции ниже

    # проверка содержания
    if day > 0:
        my_result = f'{day} дн {hours} час {minute} мин {sec} секунд'
    elif hours > 0:
        my_result = f'{hours} час {minute} мин {sec} секунд'
    elif minute > 0:
        my_result = f'{minute} мин {sec} секунд'
    elif sec > 0:
        my_result = f'{sec} секунд'
    else:
        my_result = 'Что-то пошло не так'

    return my_result


duration = 86000
result = convert_time(duration)
print(f'Время в секундах: {duration} сек')
print(result)

# Задание 2 (Кубы)
# Уверен, что считает программа правильно, совсем не уверен, что выполнил её соблюдая все условия

def sum_list_1(my_list):
    for i in range (1, 1001, 2):
        i = i ** 3
        dataset.append(i)
    for c in dataset:
        summa = []
        c = str(c)
        for d in c:
            d = int(d)
            summa.append(d)
        v = sum(summa)
        if v % 7 == 0:
            c = int(c)
            my_list.append(c)
    g = sum(my_list)
    return int(g)

def sum_list_2(my_list):
    for i in range (1, 1001, 2):
        i = i ** 3 + 17
        dataset.append(i)
    for c in dataset:
        summa = []
        c = str(c)
        for d in c:
            d = int(d)
            summa.append(d)
        v = sum(summa)
        if v % 7 == 0:
            c = int(c)
            my_list.append(c)
    g = sum(my_list)
    return int(g)

dataset = []
my_list = []

result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)

# Задание 3 (Склонения)
def transform_string(number):
    procent = [1, 31, 41, 51, 61, 71, 81, 91]
    procenta = [2, 3, 4, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]
    if n in procent:
        o = f'{n} процент'
    elif n in procenta:
        o = f'{n} процента'
    else:
        o = f'{n} процентов'
    return o

for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
