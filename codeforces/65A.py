n = int(input())
s = [0] * 3
for i in range(n):
    v1, v2, v3 = map(int, input().split())
    s[0] += v1
    s[1] += v2
    s[2] += v3
if s[0] == 0 and s[1] == 0 and s[2] == 0:
    print("YES")
else:
    print("NO")