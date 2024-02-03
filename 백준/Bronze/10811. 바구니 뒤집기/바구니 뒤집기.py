import sys

n, m = map(int, sys.stdin.readline().split())
list = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    list[i-1:j] = reversed(list[i-1:j])

for i in range(n):
    print(list[i], end=" ")