n, m = map(int, input().split())
a = list(map(int, input().split()))

s = set()
suf = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    val = a[i]
    if val in s:
        suf[i] = suf[i + 1]
    else:
        suf[i] = suf[i + 1] + 1
        s.add(val)

for i in range(m):
    print(suf[int(input()) - 1])