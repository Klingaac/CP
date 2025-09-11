n = int(input())
s = input()

sumPrefix = [0] * (n + 1)
for i in range(n):
    sumPrefix[i + 1] = sumPrefix[i] + int(s[i])

#print(sumPrefix)

minChange = float('inf')
for i in range(n - 1):
    onesToChange = sumPrefix[i + 1]
    zerosToChange = (n - (i + 1)) - (sumPrefix[n] - onesToChange)
    #print(f"{onesToChange} + {zerosToChange}")
    minChange = min(minChange, onesToChange + zerosToChange)

print(minChange)

# O(n)