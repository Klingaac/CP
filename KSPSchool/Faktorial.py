def trailing_zeros(n):
    count = 0
    p = 5
    while (p <= n):
        count += n // p
        p *= 5
    return count

l, r = 0, 4 * 10**8
k = int(input())

while (l + 1 != r):
    s = (l + r) // 2
    zeros = trailing_zeros(s)
    if k > zeros:
        l = s
    else:
        r = s

leastZeros = trailing_zeros(r)
ans = r
while trailing_zeros(ans) == leastZeros:
    ans -= 1
print(ans + 1)