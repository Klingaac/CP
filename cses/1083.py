n = int(input())
a = list(map(int, input().split()))
a.sort()

def solve(n, a):
    for i in range(n-1):
        #print(f"{i+1},{a[i]}")
        if a[i] != i+1:
            return i + 1
    return n

print(solve(n, a))
    
