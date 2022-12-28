#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
#2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

def get_factors(n):
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
    return factors

print(get_factors(6))  # [2, 3]
print(get_factors(12))  # [2, 2, 3]
print(get_factors(32))  # [2, 2, 2, 2, 2]
print(get_factors(13))  # [13]
print(get_factors(9))  # [3, 3]
print(get_factors(18))  # [2, 3, 3]
print(get_factors(21))  # [3, 7]