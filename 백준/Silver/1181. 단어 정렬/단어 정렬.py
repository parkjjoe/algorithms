import sys

n = int(sys.stdin.readline())
c = [str(sys.stdin.readline().rstrip()) for _ in range(n)]

c = list(set(c))
c.sort(key = lambda x: (len(x), x))

for i in c:
    print(i)