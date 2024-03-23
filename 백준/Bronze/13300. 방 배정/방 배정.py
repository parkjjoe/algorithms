import sys
from math import ceil

n, k = map(int, sys.stdin.readline().split())
student = [[0, 0] for _ in range(6)]
room = 0

for _ in range(n):
	s, y = map(int, sys.stdin.readline().split())
	student[y - 1][s] += 1

for i in range(6):
	for j in range(2):
		room += ceil(student[i][j] / k)

print(room)