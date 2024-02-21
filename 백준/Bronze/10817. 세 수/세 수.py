import sys

a, b, c = map(int, sys.stdin.readline().split())

num = []
num.append(a)
num.append(b)
num.append(c)

num.sort()

print(num[1])