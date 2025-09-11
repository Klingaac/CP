n = int(input())
a = list(map(int, input().split()))

moves = 0
changes = 1
while changes > 0:
    changes = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            diff = a[i-1] - a[i]
            a[i] += diff
            moves += diff
            changes += diff

print(moves)