# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

from random import randint

A = int(input('Введите сколько строк: '))
B = int(input('Введите длинну строки: '))

a = [[randint(1, 10) for j in range(B)] for i in range(A)]
print(a)

sum_row = []
sum_nums = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        sum_nums = sum_nums + a[i][j]
    sum_nums = sum_nums / len(a[i])
    sum_row.append(sum_nums)
    sum_nums = 0

for i in range(len(a)): 
    print(f'средне-арифметическое строки {i + 1} равна {sum_row[i]}')
