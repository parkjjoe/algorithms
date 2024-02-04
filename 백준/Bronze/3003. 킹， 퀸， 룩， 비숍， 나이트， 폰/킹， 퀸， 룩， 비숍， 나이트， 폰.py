import sys

total = [1, 1, 2, 2, 2, 8]
n = list(map(int, sys.stdin.readline().split()))

for i in range(6):
    total[i] = total[i] - n[i]
    print(total[i], end = " ")