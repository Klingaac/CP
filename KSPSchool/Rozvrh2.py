# velmi skaredy kod, mal by som sa k tomuto dakedy vratit

n, q = map(int, input().split())
zOc, kOc = {}, {}
s = set()

for i in range(n):
    z, k = map(int, input().split())

    s.add(z)
    s.add(k)

    zOc[z] = zOc.get(z, 0) + 1
    kOc[k] = kOc.get(k, 0) + 1

qs = list(map(int, input().split()))

cur = 0
classes = [(0, 0)]
ans = []
totalTime = 0

for t in sorted(s):
    totalTime = t
    if t in zOc:
        cur += zOc[t]
    classes.append((t, cur))
    if t in kOc:
        cur -= kOc[t]
    classes.append((t + 0.01, cur))

classes.append((totalTime + 1, 0))
classes.append((totalTime + 2, 0))

startL, startR = 0, len(classes) - 1
for t in qs:

    l, r = startL, startR
    while l + 1 < r:
        s = (l + r) // 2
        if classes[s][0] > t:
            r = s
        else:
            l = s
    ans.append(classes[l][1])

print(" ".join(map(str, ans)))


