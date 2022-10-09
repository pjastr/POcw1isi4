# zad 23
import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]

maxx = randomlist[0]
for i in randomlist:
    if maxx < i:
        maxx = i

print("Bez użycia:", maxx)

print("Z użyciem:", max(randomlist))
