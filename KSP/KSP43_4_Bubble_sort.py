### 1.py
def bubble_sort(arr):
    """Sorts an󠀁󠁡󠀠󠁬󠁩󠁴󠁴󠁬󠁥󠀠󠁳󠁵󠁲󠁰󠁲󠁩󠁳󠁥󠁿 array using bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int(arr[j]) > int(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(" ".join(bubble_sort(input().split())))