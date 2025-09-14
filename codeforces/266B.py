n, t = map(int, input().split())
s = input()
a = [i for i in s]
for _ in range(t):
    action = False
    for i in range(n - 1):
        if a[i] == "B" and a[i + 1] == "G" and not action:
            a[i], a[i + 1] = "G", "B"
            action = True
        else:
            action = False
print("".join(a))