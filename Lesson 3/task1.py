#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        result += my_list[i]

print(result)