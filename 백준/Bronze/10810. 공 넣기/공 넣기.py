import sys

n, m = map(int, sys.stdin.readline().split())
list = [0] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for a in range(i, j+1):
        list[a-1] = k

for b in range(n):
    print(list[b], end=" ")