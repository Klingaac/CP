lii = lambda: list(map(int, input().split()))

nmk = lii()
n = nmk[0] # num of elements in a
m = nmk[1] # num of operations
k = nmk[2] # num of queries, operations are 1 index

a = lii()
ops = [0] * (m)
for i in range(m):
    ops[i] = lii()

grad = [0] * (n + 1)
for i in range(0, n):
    if i == 0:
        grad[i] = a[i]
    else:
        grad[i] = a[i] - a[i-1]

cntGrad = [0] * (m + 1)
for i in range(k):
    q = lii()
    x = q[0] -1
    y = q[1] -1

    cntGrad[x] += 1
    cntGrad[y + 1] -= 1

cnt = [cntGrad[0]]
for i in range(1, m):
    cnt.append(cntGrad[i] + cnt[i-1])

for i, op in enumerate(ops):
    l, r, d = op[0] - 1, op[1] - 1, op[2] * cnt[i]
    grad[l] += d
    grad[r+1] -= d

newArr = [grad[0]]
for i in range(1, n):
    newArr.append(grad[i] + newArr[i-1])

print(" ".join(map(str, newArr)))




    # for j in range(x - 1, y):
    #     op = ops[j]
    #     l, r, d = op[0] - 1, op[1] - 1, op[2]
    #     grad[l] += d
    #     grad[r+1] -= d