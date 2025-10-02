n, p = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) < p:
    print("Nic nedostanete")
else:
    l, r = 0, 10**9
    while l + 1 != r:
        x = (l + r) // 2
        total = 0
        for child in a:
            total += min(child, x)
        if total < p:
            l = x
        else:
            r = x

    print(r)

