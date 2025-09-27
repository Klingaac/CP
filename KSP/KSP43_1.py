s = input()
n = len(s)
headFound = False
cur = 0
lenSum = 0

for i in range(n):
  l = s[i]
  if cur > 0:
    if not headFound and l == "O":
      headFound = True
      continue
    elif l == "=":
      cur += 1
    elif l == ">":
      lenSum += cur + 1
      cur = 0
    else:
      cur = 0
  if l == "~" and i + 1 < n and s[i+1] == "O": 
    cur = 1
    headFound = False

print(lenSum)

# O(n)