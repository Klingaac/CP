from math import ceil

l = input().split()
n = int(l[0])
m = int(l[1])
a = int(l[2])

print(ceil(n / a) * ceil(m / a))