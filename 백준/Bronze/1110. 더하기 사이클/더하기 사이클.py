import sys

n = int(sys.stdin.readline())
num = n
count = 0

while 1:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = 10 * b + c

    count += 1

    if n == num:
        break

print(count)