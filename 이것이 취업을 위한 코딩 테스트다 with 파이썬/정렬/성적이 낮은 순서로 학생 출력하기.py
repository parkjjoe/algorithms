import sys

n = int(sys.stdin.readline())

li = []

for _ in range(n):
    name, score = map(str, sys.stdin.readline().rstrip().split())

    li.append((name, int(score)))

li.sort(key=lambda x: x[1])

for i in li:
    print(i[0], end=" ")
