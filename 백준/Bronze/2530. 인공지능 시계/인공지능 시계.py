import sys

h, m, s = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())

s += time % 60

if s >= 60:
    s -= 60
    m += 1

m += (time // 60) % 60

if m >= 60:
    m -= 60
    h += 1

h += ((time // 60) // 60) % 24

if h >= 24:
    h -= 24

print(h, m, s)