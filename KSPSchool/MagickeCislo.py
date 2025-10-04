n = int(input())

while True:
    n += 1
    x = n
    count = set()

    magic = True
    while x > 0:
        digit = x % 10
        x //= 10
        if digit in count:
            magic = False
            break
        count.add(digit)

    if magic:
        break

print(n)