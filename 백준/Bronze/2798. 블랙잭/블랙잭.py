import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))

extract = list(combinations(number, 3))
result = []
answer = []

for i in range(len(extract)):
    result.append(sum(extract[i]))

for i in range(len(result)):
    if result[i] <= m:
        answer.append(result[i])

print(max(answer))