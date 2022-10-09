tab = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
suma = 0
for i in tab:
    suma += 1
print(suma)
for x in tab:
    if x in "B":
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
