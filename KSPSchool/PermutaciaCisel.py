from itertools import permutations

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(input())

b = [i for i in range(0, k)]


ans = float("inf")
for p in permutations(b, k):
    minn = 999999999
    maxx = -999999999
    
    for old_s in a:
        new_s_list = [0] * k
        for i, j in enumerate(p):
            new_s_list[j] = old_s[i]
        new_i = int("".join(new_s_list))
        
        maxx = max(maxx, new_i)
        minn = min(minn, new_i)

    ans = min(ans, maxx - minn)

print(ans)