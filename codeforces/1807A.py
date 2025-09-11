t = int(input())

for i in range(t):
    p = input().split()
    a = int(p[0])
    b = int(p[1])
    c = int(p[2])

    if a + b == c:
        print("+")
    else:
        print("-")