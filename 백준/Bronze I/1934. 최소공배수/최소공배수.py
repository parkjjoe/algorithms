import sys
from math import lcm

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))