n, d = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = 0

for i in range(n):
    ok = True
    if i - 1 >= 0 and a[i] - a[i - 1] <= d:
        ok = False
    if i + 1 < n and a[i + 1] - a[i] <= d:
        ok = False
    if ok:
        ans += 1

print(ans)

