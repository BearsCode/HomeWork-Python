import math

x1 = float(input("Введите координату X первой точки: "))
y1 = float(input("Введите координату Y первой точки: "))

x2 = float(input("Введите координату X второй точки: "))
y2 = float(input("Введите координату Y второй точки: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Расстояние между двумя точками равно {distance:.2f}.")