n = int(input())
arr = list(map(int, input().split()))
m = int(input())
qs = list(map(int, input().split()))

hash = {}
for i, el in enumerate(arr):
    hash[el] = i

startTotal = 0
endTotal = 0
for q in qs:
    startTotal += hash[q] + 1
    endTotal += n - hash[q]

print(startTotal, endTotal)
