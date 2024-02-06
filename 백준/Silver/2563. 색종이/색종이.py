import sys

n = int(sys.stdin.readline())
array = [[0] * 100 for _ in range(100)] # 도화지를 0으로 채움.
area = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            array[i][j] = 1 # 색종이가 있으면 0을 1로 바꿈.

for i in range(100):
    area += array[i].count(1) # 도화지에서 1의 개수를 셈.

print(area)