import sys

n = int(sys.stdin.readline())
c = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    c.append([a, b])
    
c.sort()

for i in c:
    print(i[0], i[1])