import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n = str(a * b * c)

for i in number:
    print(n.count(str(i)))