#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def get_unique_elements(lst):
    return list(set(lst))

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = get_unique_elements(lst)
print(f"Список из неповторяющихся элементов: {new_lst}")
