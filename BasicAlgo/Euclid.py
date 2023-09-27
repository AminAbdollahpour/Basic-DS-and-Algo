def euclid(n, m):
    if m == 0:
        return n
    else:
        return euclid(m, n % m)
