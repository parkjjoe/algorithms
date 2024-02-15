import sys
import math

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

up = a * d + b * c
down = b * d

result = math.gcd(up, down)
up //= result
down //= result

print(up, down)