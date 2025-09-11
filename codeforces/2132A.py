t = int(input())

for i in range(t):
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    c = input()

    for j in range(m):
        if c[j] == "D":
            a = a + b[j]
        else:
            a = b[j] + a

    print(a)