import sys
from itertools import combinations

height = [int(sys.stdin.readline()) for _ in range(9)]

hundred = list(combinations(height, 7))

for i in range(len(hundred)):
    if sum(hundred[i]) == 100:

        for j in sorted(hundred[i]):
            print(j)
        break