#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fibonacci(n):
    if n < 0:
        return fibonacci(-n)[::-1] * (-1 if n % 2 != 0 else 1)
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[-1] + fib[-2])
        return fib

n = 10
print(fibonacci(n))  # Должно вывести [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

n = -10
print(fibonacci(n))  # Должно вывести [0, -1, 1, -2, 3, -5, 8, -13, 21, -34]