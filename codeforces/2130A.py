
        
def sum(T: list):
    s = 0
    for el in T:
        s += el
    return s

t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    score = 0

    score = sum(s) + s.count(0)

    print(score)        

