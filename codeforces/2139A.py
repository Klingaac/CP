t = int(input())
for _ in range(t):
    ab = list(map(int, input().split()))
    a = ab[0]
    b = ab[1]

    if a == b:
        print(0)
    elif a % b == 0 or b % a == 0:
        print(1)
    else:
        print(2)