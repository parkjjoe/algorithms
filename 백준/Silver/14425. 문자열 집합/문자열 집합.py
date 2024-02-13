import sys

n, m = map(int, sys.stdin.readline().split())

s = []
check = []
count = 0

for _ in range(n):
    s.append(str(sys.stdin.readline().rstrip()))

for _ in range(m):
    check.append(str(sys.stdin.readline().rstrip()))

for i in range(len(check)):
    if check[i] in s:
        count += 1

print(count)