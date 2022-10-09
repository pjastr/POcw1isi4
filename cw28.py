# cw28
import random

random.seed(164439)
randomlist = [random.randrange(1, 101) for i in range(200)]
liczba = randomlist[0]
powtorzenia = 0

for i in randomlist:
    if randomlist.count(i) > powtorzenia:
        liczba = i
        powtorzenia = randomlist.count(i)

print(liczba)
print(powtorzenia)
