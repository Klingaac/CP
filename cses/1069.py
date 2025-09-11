s = input()
letter = None
cur = 0
best = 0

for i in range(len(s)):
    l = s[i]
    if l != letter:
        best = max(best, cur)
        cur = 0
        letter = l
    cur += 1

print(max(best, cur))