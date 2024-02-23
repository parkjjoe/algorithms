import sys

n = int(sys.stdin.readline())

for _ in range(n):
    p = int(sys.stdin.readline())

    dict = {}

    for _ in range(p):
        c, name = map(str, sys.stdin.readline().rstrip().split())

        dict[name] = int(c)

    print(max(dict, key=dict.get))