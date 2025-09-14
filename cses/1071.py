t = int(input())
for i in range(t):
    y, x = map(int, input().split())
    m = max(y, x)
    val = pow(m - 1, 2)
    if m % 2 == 0:
        if x == m:
            val += y
        else:
            val += m + (m - x)
    else:
        if y == m:
            val += x
        else:
            val += m + (m - y)
    print(val)