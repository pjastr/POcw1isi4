x = input("wpisz palindrom\n")


def palindrom(x):
    return x == x[::-1]


ans = palindrom(x)
if ans:
    print("Yes")
else:
    print("No")
