t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = []
    for j in range(n):
        b.append(n+1-a[j])

    print(" ".join(map(str, b)))