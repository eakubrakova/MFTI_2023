from collections import OrderedDict

def check(temps):
    # сортировка списка temps по второму элементу каждого кортежа
    sorted_temps = sorted(temps, key=lambda x: x[1], reverse=True)
    
    # создание словаря с отсортированными значениями
    result = OrderedDict(sorted_temps)
    
    # вывод словаря
    print(result)

# пример списка temps
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

# вызов функции check
check(temps)
