n = int(input())

out = []
for i in range(2, n + 1, 2):
    out.append(i)
for i in range(1, n + 1, 2):
    out.append(i)

if n == 2 or n == 3:
    print("NO SOLUTION")
else: 
    print(" ".join(map(str, out)))