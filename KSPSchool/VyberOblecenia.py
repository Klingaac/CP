from itertools import combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))
hodi = {}
for i in range(m):
    x, y = map(int, input().split())
    x, y = a[x-1], a[y-1]
    if not x in hodi:
        hodi[x] = set()
    hodi[x].add(y)
    if not y in hodi:
        hodi[y] = set()
    hodi[y].add(x)


ans = float("inf")
#print(hodi)
for c in combinations(a, 3):
    #print(c)
    if c[1] in hodi.get(c[0], []) and c[2] in hodi.get(c[0], []) and c[2] in hodi.get(c[1], []):
        #print("yes")
        ans = min(ans, sum(c))

if ans == float("inf"):
    print(-1)
else:
    print(ans)

