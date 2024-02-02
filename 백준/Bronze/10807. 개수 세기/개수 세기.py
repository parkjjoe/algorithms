import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
i = int(sys.stdin.readline())

print(l.count(i))