import sys

n, m = map(int, sys.stdin.readline().split())
a = []
b = []

for i in range(n):
    matrix = list(map(int, sys.stdin.readline().split()))
    a.append(matrix)

for i in range(n):
    matrix2 = list(map(int, sys.stdin.readline().split()))
    b.append(matrix2)

for x in range(n):
    for y in range(m):
        print(a[x][y] + b[x][y], end = " ")
    print()