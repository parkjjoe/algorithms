import sys

a, b = map(int, sys.stdin.readline().split())

n = max(a, b) - min(a, b) - 1

if max(a, b) - min(a, b) <= 1:
    n = 0

print(n)

for i in range(min(a, b) + 1, max(a, b)):
    print(i, end=" ")