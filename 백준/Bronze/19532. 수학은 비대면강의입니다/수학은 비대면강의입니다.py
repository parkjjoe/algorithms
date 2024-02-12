import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

x = int((b * f - c * e) / (b * d - a * e))
y = int((c * d - a * f) / (b * d - a * e))

print(x, y)