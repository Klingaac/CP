n, m = map(int, input().split())
cities = (list(map(int, input().split())))
towers = (list(map(int, input().split())))

ans = 0
for i, c in enumerate(cities):

    l, r = 0, m - 1

    # binary search, find the left closes tower to city
    while l + 1 < r:
        s = (l + r) // 2
        if towers[s] <= c:
            l = s
        else: 
            r = s

    # get closest left and right tower
    leftTower = towers[l]
    rightTower = towers[min(l + 1, m - 1)]

    # get their dist from city
    leftDist = abs(leftTower - c)
    rightDist = abs(rightTower - c)

    dist = min(leftDist, rightDist)
    ans = max(ans, dist)

print(ans)