# construct matrix
x = 0
y = 0
for i in range(5):
    row = list(map(int, input().split()))
    for j, el in enumerate(row):
        if el == 1:
            x = i
            y = j

dist_x = abs(2 - x)
dist_y = abs(2 - y)
print(dist_x + dist_y)
            


