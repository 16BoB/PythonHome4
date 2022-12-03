# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
from random import randint

a = [randint(1, 10) for j in range(30)]

print(a)

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min_num = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_num]:
                min_num = j
        arr[i], arr[min_num] = arr[min_num], arr[i]

selection_sort(a)

print(a)