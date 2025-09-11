n_k_list = input().split()
n = int(n_k_list[0])
k = int(n_k_list[1])

scores = input().split()
advance = 0
k_val = int(scores[k - 1])

for i in range(n):
    score = int(scores[i])
    if score >= k_val and score > 0:
        advance += 1
    else:
        break

print(advance)