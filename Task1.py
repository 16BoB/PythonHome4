# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_list_pos(arr):
    len_list = len(arr)
    sum_num = 0
    for i in range(len_list):
        if i%2 != 0:
             sum_num = sum_num + arr[i]
    return sum_num

arr = [2, 3, 5, 9, 3]

print(sum_list_pos(arr))