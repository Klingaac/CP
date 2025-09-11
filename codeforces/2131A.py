import sys
input = lambda: sys.stdin.readline().rstrip()
lii = lambda: list(map(int, input().split()))
ii = lambda: int(input())

t = ii()

for i in range(t):
    n = ii()
    l1 = lii()
    l2 = lii()

    steps = 1
    for j in range(n):
        s = max(l1[j] - l2[j], 0)
        steps += s

    print(steps)