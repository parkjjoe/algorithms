import sys

list = []

for i in range(10):
    a = int(sys.stdin.readline())
    b = a % 42
    list.append(b)

print(len(set(list)))