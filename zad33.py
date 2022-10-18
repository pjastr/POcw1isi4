import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]

print("Zadanie 33")
randomlist = list(set(randomlist))
print(len(randomlist))
