import sys
input = lambda: sys.stdin.readline().rstrip()  # Remove the newline character at the end of the line
II = lambda: int(input())
lii = lambda: list(map(int, input().split()))

nx = lii()
n = nx[0]
x = nx[1]
arr = lii()

ans = 0

h = {0: 1}
running_sum = 0

for el in arr:
    running_sum += el
    ans += h.get(running_sum - x, 0)
    h[running_sum] = h.get(running_sum, 0) + 1

print(ans)