from sys import stdin, stdout

n = int(input())
arr = list(map(int, stdin.readline().split()))

s = set(arr)
print(len(s))