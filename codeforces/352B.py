n = int(input())
a = list(map(int, input().split()))

dVals = {}
dIndice = {}
for i, x in enumerate(a):
    if not x in dVals:
        dVals[x] = 0
    elif dVals[x] == -1:
        continue
    elif dVals[x] == 0:
        dVals[x] = i - dIndice[x]
    elif i - dIndice[x] != dVals[x]:
        dVals[x] = -1
    dIndice[x] = i

ans = []
for key, val in dVals.items():
    if val != -1:
        ans.append((key, val))

ans.sort()
print(len(ans))
for s in ans:
    print(s[0], s[1])