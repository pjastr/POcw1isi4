import random

random.seed(123456)
lista = [random.randrange(1, 101) for i in range(200)]
lista2 = []

print(f"Lista z polecenia: {lista}")

for x in lista:
    if lista.count(x) == 1:
        if x not in lista2:
            lista2.append(x)

lista2.sort()
print(f"Lista bez duplikatow: {lista2}")