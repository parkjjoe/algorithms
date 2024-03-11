import sys

n, m = map(int, sys.stdin.readline().split())

num = []

def backtracking(a):
    if len(num) == m:
        print(" ".join(map(str, num)))
        return

    for i in range(a, n + 1):
        if i not in num:
            num.append(i)
            backtracking(i + 1)
            num.pop()

backtracking(1)

# import sys
# from itertools import combinations
#
# n, m = map(int, sys.stdin.readline().split())
#
# num = [i for i in range(1, n + 1)]
#
# array = list(combinations(num, m))
#
# for i in array:
#     for j in i:
#         print(j, end=" ")
#     print()