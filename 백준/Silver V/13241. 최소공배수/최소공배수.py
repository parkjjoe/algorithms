import sys
from math import lcm

a, b = map(int, sys.stdin.readline().split())

print(lcm(a, b))