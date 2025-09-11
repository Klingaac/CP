t = int(input())

def solve(n, l):
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] == l[j]:
                print("YES")
                return
    print("NO")

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    solve(n, l)
