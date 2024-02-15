import sys

n, m = map(int, sys.stdin.readline().split())

a = set()
b = set()

a.update(map(int, sys.stdin.readline().split()))
b.update(map(int, sys.stdin.readline().split()))

print(len(a - b) + len(b - a))