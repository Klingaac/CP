import itertools

n, l = map(int, input().split())
a = list(map(int, input().split()))

k = 2**n
dic = []
for i in range(n):
    b = [0] * k

    islands = 2**(i + 1) // 2
    land = k // (islands * 2)

    for j in range(islands):
        start = 2 * land * j
        for o in range(start, start + land):
            b[o] = a[i]

    dic.append(b)

#print(dic)
ans = 0

for i in range(k):
    s = 0
    for j in range(n):
        s += dic[j][i]
    if s == l:
        els = []
        for j in range(n):
            val = dic[j][i]
            if val > 0:
                els.append(val)
        print(els)


    





