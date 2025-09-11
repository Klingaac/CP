t = int(input())

for i in range(t):
    n = int(input())
    ans = 1
    j = 1
    while (j != n):
        ans += 1
        while (ans % 3 == 0 or ans % 10 == 3):
            ans += 1
        j += 1
    print(ans)