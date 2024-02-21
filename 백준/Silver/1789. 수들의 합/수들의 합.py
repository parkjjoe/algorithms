import sys

s = int(sys.stdin.readline())

sum = 0
num = 1
count = 0

while sum <= s:
    sum += num
    num += 1
    count += 1

print(count - 1)