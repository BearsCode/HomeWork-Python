#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

import random

def generate_polynomial(k):
    coefficients = [random.randint(0, 100) for _ in range(k+1)]
    
    polynomial = ''
    for i in range(k, -1, -1):
        if i == 0:
            polynomial += f"{coefficients[i]}"
        else:
            polynomial += f"{coefficients[i]}*x^{i} + "
    return polynomial

k = 6
print(generate_polynomial(k))