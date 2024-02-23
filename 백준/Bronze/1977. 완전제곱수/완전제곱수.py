import sys
from math import sqrt

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

square = []

for i in range(m, n + 1):
    if sqrt(i).is_integer():
        square.append(i)

if square:
    print(sum(square))
    print(min(square))
else:
    print(-1)