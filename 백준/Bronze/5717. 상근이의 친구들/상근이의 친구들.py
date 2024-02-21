import sys

while 1:
    m, f = map(int, sys.stdin.readline().split())

    if m == f == 0:
        break

    print(m + f)