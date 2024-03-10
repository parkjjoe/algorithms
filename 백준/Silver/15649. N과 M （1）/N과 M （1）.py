import sys

n, m = map(int, sys.stdin.readline().split())
array = []

def backtracking():
    if len(array) == m:
        print(" ".join(map(str, array)))
        return

    for i in range(1, n + 1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()

backtracking()

# import sys
# from itertools import permutations
# 
# n, m = map(int, sys.stdin.readline().split())
# array = [i for i in range(1, n + 1)]
# 
# result = list(permutations(array, m))
# 
# for i in result:
#     for j in i:
#         print(j, end=" ")
#     print()