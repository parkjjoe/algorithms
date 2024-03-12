import sys

n, m = map(int, sys.stdin.readline().split())

num = []

def backtracking():
    if len(num) == m:
        print(" ".join(map(str, num)))
        return

    for i in range(1, n + 1):
        num.append(i)
        backtracking()
        num.pop()

backtracking()

# import sys
# from itertools import product
#
# n, m = map(int, sys.stdin.readline().split())
#
# num = [i for i in range(1, n + 1)]
#
# array = list(product(num, repeat=m))
#
# for i in array:
#     for j in i:
#         print(j, end=" ")
#     print()