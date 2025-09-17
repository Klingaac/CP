from math import sqrt

ans = 0
n, m = map(int, input().split())
for a in range(0, int(sqrt(n)) + 1):
    s = pow(a, 2)
    b = n - s
    if pow(b, 2) + a == m:
        ans += 1
print(ans)