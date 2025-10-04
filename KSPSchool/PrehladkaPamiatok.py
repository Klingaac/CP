import itertools

n = int(input())
a = list(map(int, input().split()))
ans = 0

permutations = itertools.permutations(a)

for per in permutations:
    x = 0
    for e in per:
        x += e
        if x < 0:
            break
    if x > 0:
        ans += 1

print(ans)