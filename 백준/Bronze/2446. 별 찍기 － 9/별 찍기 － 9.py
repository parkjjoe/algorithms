import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(" " * i + "*" * (2 * n - 2 * i - 1))

for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))