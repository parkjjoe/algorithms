import sys

n = int(sys.stdin.readline())

li = []

for _ in range(n):
    name, l, e, m = map(str, sys.stdin.readline().rstrip().split())

    li.append((name, int(l), int(e), int(m)))

li = sorted(li, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in li:
    print(i[0])