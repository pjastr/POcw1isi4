# zad 22
import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]

mini = randomlist[0]
for i in randomlist:
    if mini > i:
        mini = i

print("Bez użycia:", mini)

print("Z użyciem:", min(randomlist))
