n = int(input())
v = list(map(int, input().split()))
sort_v = v.copy()
sort_v.sort()

pref_v = [0]
for i in range(1, len(v) + 1):
    pref_v.append(pref_v[i-1] + v[i-1])

pref_sort_v = [0]
for i in range(1, len(v) + 1): 
    pref_sort_v.append(pref_sort_v[i-1] + sort_v[i-1])

m = int(input())
for j in range(m):
    t, l, r = map(int, input().split())
    ans = 0
    if t == 1:
        ans = pref_v[r] - pref_v[l - 1]
    else:
        ans = pref_sort_v[r] - pref_sort_v[l - 1]
    print(ans)