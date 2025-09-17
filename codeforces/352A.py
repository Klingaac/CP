n = int(input())
cards = list(map(int, input().split()))
fCards, zCards = 0, 0
for c in cards:
    if c == 5:
        fCards += 1
zCards = n - fCards

if fCards < 9 or zCards == 0:
    if zCards == 0:
        print(-1)
    else:
        print(0)
else:
    print('5' * (fCards - fCards % 9 ) + '0' * zCards)