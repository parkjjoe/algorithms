import sys

n, k = map(int, sys.stdin.readline().split())

circle = [i for i in range(1, n + 1)]
answer = []
num = 0

for _ in range(n):
  num += k - 1

  if num >= len(circle):
    num %= len(circle)

  answer.append(str(circle.pop(num)))
print("<", ", ".join(answer)[:], ">", sep="")