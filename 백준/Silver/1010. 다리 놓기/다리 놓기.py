import sys
from math import factorial

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    print(int(factorial(m) / (factorial(n) * factorial(m - n))))