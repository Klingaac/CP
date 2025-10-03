n = int(input())
zOc, kOc = {}, {}
s = set()
for i in range(n):
    z, k = map(int, input().split())

    s.add(z)
    s.add(k)

    zOc[z] = zOc.get(z, 0) + 1
    kOc[k] = kOc.get(k, 0) + 1

most = 0
cur = 0

for e in sorted(s):
    if e in zOc:
        cur += zOc[e]
    most = max(most, cur)
    if e in kOc:
        cur -= kOc[e]

print(most)

    

