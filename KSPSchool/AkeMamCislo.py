a, b, n = map(int, input().split())

def solve(x: int) -> int:
    if x == 1:
        return a
    elif x == 2: 
        return b
    
    return solve(x - 1) + solve(x - 2)

print(solve(n))