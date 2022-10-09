#   zad 36
import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]

lista3 = []
for x in randomlist:
    if x % 2 == 0:
        lista3.append(x)

print(len(lista3))
