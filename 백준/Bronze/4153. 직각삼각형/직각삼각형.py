import sys

while 1:
    num = sorted(list(map(int, sys.stdin.readline().split())))

    if sum(num) == 0: break

    if num[0] ** 2 + num[1] ** 2 == num[2] ** 2: print("right")
    else: print("wrong")