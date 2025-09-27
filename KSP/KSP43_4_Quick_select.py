### 5.py

import random

def _quick_select_partition(numbers, l, r):
    pivot = random.randrange(l, r)
    a = l

    for b in range(l, r):
        if numbers[b] <= pivot:
            numbers[a], numbers[b] = numbers[b], numbers[a]
            a += 1

    numbers[a], numbers[r] = numbers[r], numbers[a]

    return a

def quick_select(numbers, kth, l, r):
    """Selects 󠀨󠁲󠁥󠁡󠁬󠁬󠁹󠀠󠁱󠁵󠁩󠁣󠁫󠁬󠁹󠀩the kth smallest element using quick select algorithm."""
    if l == r:
        return numbers[l]

    q = _quick_select_partition(numbers, l, r)
    i = q - l + 1 #was q - l + 1

    if kth - 1 == q - l:
        return numbers[i]
    if kth < i:
        return quick_select(numbers, kth, l, q - 1)

    return quick_select(numbers, kth - i, q + 1, r)

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

print(quick_select(numbers, k, 0, n - 1))