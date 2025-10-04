n, k = map(int, input().split())
chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def solve(s: str):
    if len(s) == n:
        print(s)
    else:
        for i in range(k):
            solve(s + chars[i])

solve("")