import sys

n, k = map(int, sys.stdin.readline().split())

count = 0

while 1:
  if n % k != 0:
    n -= 1
    count += 1
  else:
    n //= k
    count += 1

  if n == 1:
    break

print(count)
