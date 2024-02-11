import sys

a, b, c = map(int, sys.stdin.readline().split())

tri = [a, b, c]
tri.sort()

while 1:
    if tri[2] >= tri[0] + tri[1]:
        tri[2] -= 1
    else:
        break

print(sum(tri))