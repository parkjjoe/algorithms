import sys

n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

y, m = 0, 0

for i in time:
    y += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15

if y == m:
    print("Y M", y)
elif y < m:
    print("Y", y)
else:
    print("M", m)