# neviem ako nato, vraj mam pouzit segment tree ale to je prilis na mna

n = int(input())
m = [[False] * 501 for _ in range(501)]
x1s, y1s, x2s, y2s = [], [], [], [],
collums = []

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1s.append(x1); y1s.append(y1), x2s.append(x2), y2s.append(y2)

for i in range(n):
    for j in range(n):
        if i == j:
            continue

