import sys

n = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

count = 0
start, end = 0, n - 1

while start < end:
    if num[start] + num[end] == x:
        count += 1
        start += 1
        end -= 1
    elif num[start] + num[end] < x:
        start += 1
    else:
        end -= 1

print(count)