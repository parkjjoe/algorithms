import sys

n, m = map(int, sys.stdin.readline().split())
number = []
result = []

for _ in range(n):
  number.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
  result.append(min(number[i]))

print(max(result))
