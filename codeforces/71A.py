n = int(input())
words = []
for i in range(n):
    words.append(input())

for i in range(n):
    word = words[i]
    l = len((word))
    if l <= 10:
        print(word)
    else:
        newWord = ""
        newWord += word[0]
        newWord += str(l - 2)
        newWord += word[l - 1]
        print(newWord)