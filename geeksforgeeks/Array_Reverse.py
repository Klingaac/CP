def countFreq(arr):
    # stores frequency of each number
    mp = {}
    # stores [number, frequency]
    ans = []

    # count frequency using dictionary
    for num in arr:
        mp[num] = mp.get(num, 0) + 1

    # Build the answer list from the frequency map
    for num, freq in mp.items():
        ans.append([num, freq])

    return ans


if __name__ == "__main__":
    arr = [10, 20, 10, 5, 20]

    ans = countFreq(arr)

    # sort the result in ascending order of the number
    ans.sort(key=lambda x: x[0])

    for x in ans:
        print(x[0], x[1])




a = [4324, 5324, 523]

str(a)