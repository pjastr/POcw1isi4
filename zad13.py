def ciag_geo(n, a1=1, q=2):
    if n == 1:
        return a1
    else:
        return ciag_geo(n - 1, q, a1) * q


print(ciag_geo(10))
