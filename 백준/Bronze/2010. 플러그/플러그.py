import sys

n = int(sys.stdin.readline())

count = 0

for _ in range(n):
    a = int(sys.stdin.readline())

    count += a

print(count - (n - 1))