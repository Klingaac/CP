n = int(input())
a = list(map(int, input().split()))

b = []
for i in range(n):
    if a[i] == 0:
        b.append(+1)
    else:
        b.append(-1)

S = sum(a[0:n + 1])
best = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        best = max(best, S + sum(b[i:j]))

print(best)