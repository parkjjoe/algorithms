import sys

x = []
y = []

for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)

for i in range(3): # 직사각형이 되려면 네 점의 x, y 좌표가 동일한 숫자로 2개씩 있어야 한다.
    if x.count(x[i]) == 1: x4 = x[i]
    if y.count(y[i]) == 1: y4 = y[i]

print(x4, y4)