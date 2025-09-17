n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
b.reverse()

maxRatio = 0
ratios = 0

for ai in a:
    for bi in b:
        ratio = bi / ai
        if ratio % 1 == 0:
            if ratio > maxRatio:
                maxRatio = ratio 
                ratios = 1
                break
            elif ratio == maxRatio:
                ratios += 1
                break
        elif ratio < maxRatio:
            break
        
print(ratios)
