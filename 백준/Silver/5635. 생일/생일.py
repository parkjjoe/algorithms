import sys

n = int(sys.stdin.readline())

li = []

for _ in range(n):
    name, dd, mm, yyyy = map(str, sys.stdin.readline().rstrip().split())
    li.append((name, int(dd), int(mm), int(yyyy)))

    li.sort(key=lambda x: (x[3], x[2], x[1]))

print(li[-1][0])
print(li[0][0])