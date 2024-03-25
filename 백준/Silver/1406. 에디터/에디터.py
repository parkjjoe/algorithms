import sys

n = list(sys.stdin.readline().strip())
n2 = []

for _ in range(int(sys.stdin.readline())):
  li = sys.stdin.readline().split()

  if li[0] == 'L' and n:
    n2.append(n.pop())
  elif li[0] == 'D' and n2:
    n.append(n2.pop())
  elif li[0] == 'B' and n:
    n.pop()
  elif li[0] == 'P':
    n.append(li[1])

answer = n+n2[::-1]
print(''.join(answer))