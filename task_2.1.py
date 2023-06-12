# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

# def minimum(arr):
#     pass

# def maximum(arr):
#     pass

# Нахождение максимального и минимального значения с помощью функции reduce
from functools import reduce

list1 = [4,6,2,1,9,63,-134,566]
print('Максимальное: ', reduce(max, list1))
print('Минимальное: ', reduce(min, list1))

# Поиск максимального и минимального значения перебором

def large(arr): 
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
           max_ = ele
    return max_ 

list1 = [-52, 56, 30, 29, -54, 0, -110]
result = large(list1)
print('Максимальное: ',result)

def large(arr): 
    min_ = arr[0]
    for ele in arr:
        if ele < min_:
           min_ = ele
    return min_ 

list1 = [-52, 56, 30, 29, -54, 0, -110]
result = large(list1)
print('Минимальное: ',result)
