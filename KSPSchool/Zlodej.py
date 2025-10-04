n, w = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
def solve(b: list[int], m: int):
    global ans
    if m > n - 1:
        x = sum(b)
        if x <= w:
            ans = max(ans, x)
        return
    
    solve(b, m + 1)
    c = b.copy()
    c.append(a[m])
    solve(c, m + 1)

solve([], 0)

print(ans)
    