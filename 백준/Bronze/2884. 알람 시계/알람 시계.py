import sys

a, b = map(int, sys.stdin.readline().split())

if b >= 45:
    print(a, b-45)
elif a > 0 and b < 45:
    print(a - 1, 15 + b)
else:
    print(23, 15 + b)