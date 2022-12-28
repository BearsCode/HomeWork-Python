#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

def decimal_to_binary(num):
    binary = ""
    while num > 0:
        binary += str(num % 2)
        num //= 2
    return binary[::-1]

print(decimal_to_binary(45))
print(decimal_to_binary(3))
print(decimal_to_binary(2))