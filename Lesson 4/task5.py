#*** 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
#2*x^  + 4*x      5*x^2 + 2*x
#   7x^2 + 6x
#2*x^6  + 4*x      5*x^2 + 2*x
#    2*x^6 + 5x^2 + 6x

# Открываем первый файл для чтения
with open("file1.txt", "r") as file1:
  # Читаем строку из файла
  polynomial1 = file1.read()

# Открываем второй файл для чтения
with open("file2.txt", "r") as file2:
  # Читаем строку из файла
  polynomial2 = file2.read()

# Разбиваем строки на списки мономов
polynomial1 = polynomial1.split()
polynomial2 = polynomial2.split()

# Создаем словарь для хранения суммы многочленов
result = {}

# Перебираем мономы из первого файла
for monomial in polynomial1:
  # Разбиваем моном на коэффициент и степень
  if "x^" in monomial:
    coefficient, power = monomial.split("x^")
    power = int(power)
  else:
    coefficient = int(monomial)
    power = 0

  # Суммируем коэффициенты для одинаковых степеней
  if power in result:
    result[power] += coefficient
  else:
    result[power] = coefficient

# Перебираем мономы из второго файла
for monomial in polynomial2:
  # Разбиваем моном на коэффициент и степень
  if "x^" in monomial:
    coefficient, power = monomial.split("x^")
    power = int(power)
  else:
    coefficient = int(monomial)
    power = 0

  # Суммируем коэффициенты для одинаковых степеней
  if power in result:
    result[power] += coefficient
  else:
    result[power] = coefficient

# Формируем строку с результатом
result_str = ""
for power, coefficient in sorted(result.items(), key=lambda x: x[0], reverse=True):
  if coefficient != 0:
    if power == 0:
      result_str += str(coefficient)
    else:
      result_str += f"{coefficient}x^{power} "

# Открываем файл для записи
with open("result.txt", "w") as result_file:
  # Записываем результат в файл
  result_file.write(result_str)

