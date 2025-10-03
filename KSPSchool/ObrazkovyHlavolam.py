n, k = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))

l, r = 0, 4 * 10**4 + 1
while l + 1 < r:
    s = (l + r) // 2
    
    sm = 0
    for e in a:
        sm += e // s

    if sm < n:
        r = s
    else:
        l = s

print(l)