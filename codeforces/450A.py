n, m = map(int, input().split())
arr = list(map(int, input().split()))

last = 0
while True:
    allZero = True
    for i, el in enumerate(arr):
        if el > 0:
            arr[i] -= m
            last = i
            allZero = False
    
    if allZero:
        break

print(last + 1)