# cw25 (inny sposób)
import random

random.seed(123456)
randomlist = [random.randrange(1, 101) for i in range(200)]


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                if not swapped:
                    return


posortowane1 = sorted(randomlist)
posortowane2 = randomlist
bubbleSort(posortowane2)

print(posortowane1[:20])
print(posortowane2[:20])
