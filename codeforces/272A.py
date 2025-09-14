n = int(input())
s = 0
for i in range(n):
    s += int(input())

rem = (s + 1 + 1) % (n + 1)
if rem == 0:
    print(2)
else:
    print(1)