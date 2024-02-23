import sys

n = int(sys.stdin.readline())

for i in range(n + 1):
    if n - i == 0:
        break

    print(n - i)