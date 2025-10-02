n = int(input())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    x = int(input())

    l, r = 0, n
    while l + 1 != r:
        mid = (l + r) // 2
        if a[mid] > x:
            r = mid
        else:
            l = mid

    if a[l] == x:
        print(l)
    else:
        print("-1")