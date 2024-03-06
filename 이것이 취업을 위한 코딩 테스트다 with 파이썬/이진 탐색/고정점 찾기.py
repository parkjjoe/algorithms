# 이진 탐색

import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

def binary_search(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)

index = binary_search(array, 0, n - 1)

if index == None:
    print(-1)
else:
    print(index)
########################################################
# 선형 탐색 - 시간 초과 가능성 ↑

import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

for i in range(len(array)):
    if i == array[i]:
        print(i)
        break
else:
    print(-1)
