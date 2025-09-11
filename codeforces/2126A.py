t = int(input())

for i in range(t):
    n = int(input())
    mn = 9
    while n > 0:
        mn = min(mn, n % 10)
        n //= 10
    print(mn)