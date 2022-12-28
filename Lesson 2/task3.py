#Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
#Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
#Ввод: 4
#[-4, -3, -2, -1, 0, 1, 2, 3,4]

def multiply_elements(my_list, indices):
    result = 1
    for index in indices:
        result *= my_list[index]
    return result

indices = [2, 2, 3, 1, 8]

N = 4
numbers = [i for i in range(-N, N+1)]

print(multiply_elements(numbers, indices))