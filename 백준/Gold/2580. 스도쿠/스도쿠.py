import sys

def row(r, n):
	for i in range(9):
		if n == map[r][i]:
			return False
	return True

def col(c, n):
	for i in range(9):
		if n == map[i][c]:
			return False
	return True

def square(x, y, n):
	x = x // 3 * 3
	y = y // 3 * 3

	for i in range(3):
		for j in range(3):
			if n == map[x + i][y + j]:
				return False
	return True

def solution(n):
	if n == len(blank):
		for i in range(9):
			print(*map[i])
		exit()

	x, y = blank[n][0], blank[n][1]

	for i in range(1, 10):
		if col(y, i) and row(x, i) and square(x, y, i):
			map[x][y] = i
			solution(n + 1)
			map[x][y] = 0

map = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = []

for i in range(9):
	for j in range(9):
		if map[i][j] == 0:
			blank.append((i, j))

solution(0)