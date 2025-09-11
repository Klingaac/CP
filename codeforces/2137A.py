t = int(input())
for i in range(t):
    kx = list(map(int, input().split()))
    k = kx[0]
    x = kx[1]

    x = x * pow(2, k)
    print(x)