import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(str, sys.stdin.readline().split())

    for i in range(len(b)):
        print(b[i] * int(a), end="")
    print()