t = int(input())

for i in range(t):
    p = input().split()
    a = int(p[0])
    b = int(p[1])
    c = int(p[2])

    if a + b >= 10 or a + c >= 10 or c + b >= 10:
        print("YES")
    else:
        print("NO")