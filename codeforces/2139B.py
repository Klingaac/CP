lii = lambda: list(map(int, input().split()))

t = int(input())
for _ in range(t):
    nm = lii()
    n = nm[0]
    m = nm[1]
    a = lii()
    a.sort()

    s = 0
    if m >= n:
        for el in a:
            s += el * m
        for i in range(n-1, 0, -1):
            j = n - (i + 1)
            #print(f"i:{i}, a:{a[j]}")
            s -= i * a[j]
    else:
        nmdiff = n - m - 1
        for i in range(1, m + 1):
            j = nmdiff + i
            # print(f"i:{i}, a:{a[j]}")
            s += a[j] * i

    print(s)