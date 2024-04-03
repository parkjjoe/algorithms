import sys

t = int(sys.stdin.readline())
array = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    array.append(array[i - 2] + array[i - 3])

for _ in range(t):
    n = int(sys.stdin.readline())
    print(array[n])