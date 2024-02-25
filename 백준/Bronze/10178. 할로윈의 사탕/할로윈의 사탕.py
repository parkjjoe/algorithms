import sys

t = int(sys.stdin.readline())

for _ in range(t):
    c, v = map(int, sys.stdin.readline().split())

    print("You get " + str(c // v) + " piece(s) and your dad gets " + str(c % v) + " piece(s).")