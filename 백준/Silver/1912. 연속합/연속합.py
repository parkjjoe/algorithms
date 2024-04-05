import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    number[i] = max(number[i], number[i] + number[i - 1])

print(max(number))