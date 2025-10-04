n = int(input())
m = [[False] * 501 for _ in range(501)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            m[x][y] = True

ans = 0
for x in range(501):
    for y in range(501):
        if m[x][y]:
            ans += 1

print(ans)
