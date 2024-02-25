import sys

d = int(sys.stdin.readline())
car = list(map(int, sys.stdin.readline().split()))

count = 0

for i in car:
    if d == int(i): count += 1

print(count)