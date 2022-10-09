# Zadanie 21 (drugie)
import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]
suma = 0
for i in randomlist:
    suma = i + suma

print(suma)
