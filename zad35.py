#  zad 35
import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]

a = int(input("podaj liczbe a"))
b = int(input("podaj liczbe b"))

lista3 = []
for x in randomlist:
    if a <= x <= b:
        lista3.append(x)

# print(lista3)
print(len(lista3))
