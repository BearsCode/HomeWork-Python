#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#(0,0,0), (0,0,1) и тд.

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:

       
           left = not (x or y or z)
           right = not x and not y and not z

        if left == right:
            print(f"{x}, {y}, {z}: True")
            print(f"{x}, {y}, {z}: False")
      