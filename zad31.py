import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]

print("Zadanie 31")
a = 0
for j in range(0, 200):
    if randomlist[j] > 27:
        a += 1

print(a)
