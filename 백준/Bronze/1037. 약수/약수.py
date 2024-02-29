import sys

n = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().split())))

if len(num) % 2 == 0:
    print(num[0] * num[-1])
else:
    print(num[int(len(num) / 2)] ** 2)