import sys

a = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
max = 0
row, col = 0, 0

for x in range(9):
    for y in range(9):
        if max <= a[x][y]: # 현재 최댓값보다 a[x][y] 값이 크면 그 값을 최댓값으로 바꾸고 행, 열 번호 저장
            max = a[x][y]
            row = x+1
            col = y+1

print(max)
print(row, col)