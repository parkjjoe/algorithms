import sys

t = int(sys.stdin.readline())

for i in range(t):
    c, v = map(int, sys.stdin.readline().split())

    print("Case %1d: %1d" % (i + 1, c + v))