n = int(input())
a = list(map(int, input().split()))
q = int(input())

def binary_search(x: int):
        l, r = 0, n
        while l + 1 != r:
            mid = (l + r) // 2
            if a[mid] > x:
                r = mid
            else:
                l = mid

        if a[l] == x:
            return True
        else:
            return False

for i in range(q):
    x = int(input())
    if not binary_search(x):
        if not binary_search(-x):
            print("N")
        else:
            print("A")
    else:
        print("A")    