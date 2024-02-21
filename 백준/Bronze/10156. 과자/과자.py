import sys

k, n, m = map(int, sys.stdin.readline().split())

print(k * n - m if k * n > m else 0)