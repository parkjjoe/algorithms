import sys

n = int(sys.stdin.readline())
dict = []

for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    dict.append((int(a), b))

dict.sort(key = lambda x: x[0])

for i in dict:
    print(i[0], i[1])