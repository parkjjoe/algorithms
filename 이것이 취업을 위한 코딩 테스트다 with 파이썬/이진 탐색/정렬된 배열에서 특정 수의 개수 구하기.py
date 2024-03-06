# 이진 탐색

import sys

n, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

# 정렬된 수열에서 값인 x의 원소 세는 함수
def count_by_value(array, x):
    n = len(array)
    a = first(array, x, 0, n - 1) # x가 처음 등장한 인덱스 계산

    if a == None: return 0 # x가 없으면 0개 반환

    b = last(array, x, 0, n - 1) # x가 마지막으로 등장한 인덱스 계산
    return b - a + 1

# 처음 위치 찾는 이진 탐색 함수
def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == 0 or target > array[mid - 1]) and array[mid] == target: # 해당 값을 갖는 원소 중 가장 왼쪽에 있는 경우에만 인덱스 반환
        return mid
    elif array[mid] >= target: # 중간점보다 찾는 값이 작거나 같으면 왼쪽 확인
        return first(array, target, start, mid - 1)
    else: # 중간점보다 찾는 값이 크면 오른쪽 확인
        return first(array, target, mid + 1, end)


# 마지막 위치 찾는 이진 탐색 함수
def last(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:  # 해당 값을 갖는 원소 중 가장 오른쪽에 있는 경우에만 인덱스 반환
        return mid
    elif array[mid] > target:  # 중간점보다 찾는 값이 작거나 같으면 왼쪽 확인
        return last(array, target, start, mid - 1)
    else:  # 중간점보다 찾는 값이 크면 오른쪽 확인
        return last(array, target, mid + 1, end)

count = count_by_value(array, x)

print(-1) if count == 0 else print(count)
########################################################
# bisect

import sys
from bisect import bisect_left, bisect_right

n, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

# 값이 [left_value, right_value]인 데이터의 개수 반환 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

count = count_by_range(array, x, x)

print(-1) if count == 0 else print(count)
########################################################
# count()

import sys

n, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

print(array.count(x)) if x in array else print(-1)
