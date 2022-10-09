tab = [1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
suma = 0
for i in tab:
    suma += i
print(suma)
for x in range(10):
    if x not in tab:
        print(x)
print(f"dlugosc przed odjeciem {len(tab)}")
del tab[2:5]
for i in tab:
    print(i, end=",")
print()
print(f"dlugosc po odjeciu {len(tab)}")
tab.append(4.)
for i in tab:
    print(i, end=",")
