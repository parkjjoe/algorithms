import sys

a, b = list(map(str, sys.stdin.readline().split()))
a = a[::-1]
b = b[::-1]

if int(a) > int(b):
    print(a)
else:
    print(b)