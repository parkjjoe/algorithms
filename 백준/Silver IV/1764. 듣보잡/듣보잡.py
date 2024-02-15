import sys

n, m = map(int, sys.stdin.readline().split())

hear = set()
see = set()
result = []

for _ in range(n):
    hear.add(str(sys.stdin.readline().rstrip()))

for _ in range(m):
    see.add(str(sys.stdin.readline().rstrip()))

for i in hear:
    if i in see:
        result.append(i)

result.sort()
print(len(result))

for i in result:
    print(i)