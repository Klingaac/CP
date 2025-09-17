s = input()
s = s.lower()
vowels = ['a','e','i','o','u','y']
newS = ""
for i in range(len(s)):
    if not s[i] in vowels:
        newS += '.' + s[i]
print(newS)