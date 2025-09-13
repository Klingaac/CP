### 4.py

# Dynamické programovanie - knapsack 󠀁󠁰󠁲󠁯󠁵󠁤󠁬󠁹󠀠󠁳󠁴󠁯󠁬󠁥󠁮󠀠󠁦󠁲󠁯󠁭󠀠󠁳󠁣󠁨󠁯󠁯󠁬󠀮󠁫󠁳󠁰󠀮󠁳󠁫󠁿

n, w = map(int, input().split())
ws = list(map(int, input().split()))
vs = list(map(int, input().split()))

D = [[0] * (w + 1)] * n + 1 # add + 1 to n

for i in range(1, n + 1):
    for j in range(1, w + 1):
        if ws[i - 1] > j:
            if i == 0:
                continue
            D[i][j] = D[i - 1][j]
        else:
            if i == 0:
                D[i][j] = 0
            elif w - ws[i] < 0:
                D[i][j] = D[i - 1][j]
            else:
                D[i][j] = max(D[i - 1][j], vs[i - 1] + D[i - 1][j - ws[i]])

print(D[-1][-1])