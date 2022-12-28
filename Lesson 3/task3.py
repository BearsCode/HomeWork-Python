#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def diff_fractions(lst):
    min_fraction = 1.0
    max_fraction = 0.0
    for num in lst:
        fraction = num - int(num)
        if fraction < min_fraction:
            min_fraction = fraction
        if fraction > max_fraction:
            max_fraction = fraction
    return max_fraction - min_fraction

print(diff_fractions([1.1, 1.2, 3.1, 5, 10.01]))

