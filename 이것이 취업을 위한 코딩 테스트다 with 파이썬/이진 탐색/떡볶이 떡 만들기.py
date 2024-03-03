import sys

n, m = map(int, sys.stdin.readline().split())
rice_cake = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(rice_cake)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in rice_cake:
        if i > mid: # 잘랐을 때 떡의 양 계산
            total += i - mid

    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
