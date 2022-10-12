import random

random.seed(123456)
randomlist = [random.randrange(1,101) for i in range(200)]

print("Zadanie 32")
new = randomlist.copy()
new.sort()
print("Najmniejsze liczby: ", new[0],new[1],new[2])
x = len(randomlist)
print("Najwieksze liczby: ", new[x-1],new[x-2],new[x-3])
