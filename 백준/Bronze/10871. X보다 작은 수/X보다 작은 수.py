import sys

a, b = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))

for i in range(a):
    if b > a_list[i]:
        print(a_list[i], end=" ")