import sys

n = int(sys.stdin.readline())

num = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)

for i in num:
    print(i, end=" ")
