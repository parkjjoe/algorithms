import sys

n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

count = 0
result = -1

def merge_sort(A, p, r):
    if p < r and count <= k:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    i, j, t = p, q + 1, 1
    tmp = []

    global count, result

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while  i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    i, t = p, 0

    while i <= r:
        A[i] = tmp[t]
        count += 1

        if count == k:
            result = A[i]
            break
        i += 1
        t += 1

merge_sort(array, 0, n - 1)
print(result)