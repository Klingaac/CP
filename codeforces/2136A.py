t = int(input())

for i in range(t):
    l = [int(x) for x in input().split()]
    a = l[0]
    b = l[1]
    c = l[2] - a 
    d = l[3] - b 

    if a > (b+1) * 2 or b > (a+1) * 2 or c > (d+1) * 2 or d > (c+1) * 2:
        print("NO")
    else:
        print("YES")