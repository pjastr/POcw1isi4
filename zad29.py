import random

random.seed(123456)
randomlist = [random.randrange(1,101) for i in range(200)]

print("Zadanie 29")
for i in range(0,200):
    if randomlist.count(randomlist[i]) == 1:
        print(randomlist[i])