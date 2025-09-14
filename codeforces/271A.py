y = input()
n = int(y)
i = 0
while True:
    i += 1
    arr = [i for i in str(n + i)]
    if len(set(arr)) == 4:
        print("".join(map(str, arr)))
        break