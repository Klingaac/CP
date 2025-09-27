def partition(arr, l, r):
    
    x = arr[4]
    i = l
    for j in range(l, r):
        
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    arr[i], arr[r] = arr[r], arr[i]

    print(arr)

    return i

print(partition([7, 2, 1, 9, 3, 6, 8], 0, 6))