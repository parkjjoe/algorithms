#  이진 탐색 이용
import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(sys.stdin.readline())
A = sorted(set(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in B:
    result = binary_search(A, i, 0, n - 1)

    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
################################################################
# 계수 정렬 이용
import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(sys.stdin.readline())
A = [0] * 1000001

for i in sys.stdin.readline().split():
    A[int(i)] = 1

m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in B:
    if A[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
################################################################
# 집합 자료형 이용
import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in B:
    if i in A:
        print("yes", end=" ")
    else:
        print("no", end=" ")
