# zad 27
import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]

count = 0
for i in randomlist:
    if 100 <= i <= 999:
        count = count + 1

print(count)
