n = int(input())
s = []
for i in range(n):
    s.append(tuple(map(int, input().split())))
ans = 0
for t1 in s:
    found = [False] * 4
    for t2 in s:
        if t1[0] == t2[0]:
            if t1[1] > t2[1]:
                found[0] = True
            if t1[1] < t2[1]:
                found[1] = True
        if t1[1] == t2[1]:
            if t1[0] > t2[0]:
                found[2] = True
            if t1[0] < t2[0]:
                found[3] = True      
    if not False in found:
        ans += 1 
print(ans)