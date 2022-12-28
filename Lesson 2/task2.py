#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
#Пример:
#Для n = 15: Ответ: 3
#Для n = 35: Ответ: 5

def find_smallest_divisor(n):
    for i in range(3, n, 2):
        if n % i == 0:
            return i
    return n

print(find_smallest_divisor(15))  # Должно вывести 3
print(find_smallest_divisor(35))  # Должно вывести 5
print(find_smallest_divisor(7))   # Должно вывести 7
print(find_smallest_divisor(100)) # Должно вывести 5