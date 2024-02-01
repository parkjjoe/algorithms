import sys

h, m1 = map(int, sys.stdin.readline().split())
m2 = int(sys.stdin.readline())

h += m2 // 60
m1 += m2 % 60

if m1 >= 60:
    h += 1
    m1 -= 60

if h >= 24:
    h -= 24

print(h, m1)