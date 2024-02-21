import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
house, chicken = [], []

for i in range(n):
    maps = list(map(int, sys.stdin.readline().split()))

    for j in range(n):
        if maps[j] == 1: # 집 추가
            house.append((i, j))
        elif maps[j] == 2: # 치킨집 추가
            chicken.append((i, j))

chicken_combinations = list(combinations(chicken, m)) # m개의 치킨집 뽑는 조합

# 치킨 거리 합 계산
def get_sum(chicken_combinations):
    result = 0

    for i, j in house: # 모든 집에 대해 가장 가까운 치킨집 찾기
        temp = 1e9

        for k, l in chicken_combinations:
            temp = min(temp, abs(i - k) + abs(j - l))
        result += temp # 가장 가까운 치킨집까지의 거리 더하기

    return result

# 치킨 거리의 합의 최소 출력
result = 1e9

for i in chicken_combinations:
    result = min(result, get_sum(i))

print(result)
