from math import sqrt, ceil

primes = set()

MAX = 10**6
a = [False] * (MAX + 1)
for i in range(2, ceil(sqrt(MAX) + 1)):
    if a[i] == False:
        for j in range(i*i, MAX+1, i):
            a[j] = True

for i in range(2, MAX + 1):
    if a[i] == False:
        primes.add(i)

n = int(input())
v = list(map(int, input().split()))
for i in range(n):
    if sqrt(v[i]) in primes:
        print("YES")
    else:
        print("NO")
