import sys

n, m = map(int, sys.stdin.readline().split())

num = []

def backtracking(start):
    if len(num) == m:
        print(" ".join(map(str, num)))
        return

    for i in range(start, n + 1):
        num.append(i)
        backtracking(i)
        num.pop()

backtracking(1)

# import sys
# from itertools import combinations_with_replacement
#
# n, m = map(int, sys.stdin.readline().split())
#
# num = [i for i in range(1, n + 1)]
#
# array = list(combinations_with_replacement(num, m))
#
# for i in array:
#     for j in i:
#         print(j, end=" ")
#     print()