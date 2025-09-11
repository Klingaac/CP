def solve():
    n = int(input())
    bstring = input()
    b = list(map(int, bstring.split()))

    h = {}
    for el in b:
        h[el] = h.get(el, 0) + 1

    for k, v in h.items():
        if v % k != 0:
            return -1
        
    a = []
    cnt = [0] * (n+1)
    candidate = [0] * (n+1)
    m = 0
    for x in b:
        if cnt[x] == 0:
            m += 1
            candidate[x] = m
            a.append(m)
            cnt[x] = 1
        else:
            a.append(candidate[x])
            cnt[x] += 1
        if cnt[x] == x:
            cnt[x] = 0
    if max(cnt) == 0:
        return " ".join(map(str, a))
    else:
        return -1
        

t = int(input())
for i in range(t):
    print(solve())
