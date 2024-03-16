import sys

t = int(sys.stdin.readline())

for _ in range(t):
	k = int(sys.stdin.readline())
	n = int(sys.stdin.readline())

	zero_floor = [i for i in range(1, n + 1)]

	for _ in range(k):
		for i in range(1, n):
			zero_floor[i] += zero_floor[i - 1]

	print(zero_floor[n - 1])