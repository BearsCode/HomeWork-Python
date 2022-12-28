#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

def mult_pairs(lst):
    result = []
    l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
    for i in range(l):
        result.append(lst[i] * lst[len(lst)-i-1])
    return result

print(mult_pairs([2, 3, 4, 5, 6]))
print(mult_pairs([2, 3, 5, 6]))