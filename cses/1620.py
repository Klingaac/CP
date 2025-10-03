n, t = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, 10**18

while l + 1 < r:
    s = (l + r) // 2

    sm = 0
    for e in a:
        sm += s // e

    if sm < t:
        l = s
    else:
        r = s

print(r)