import sys

for _ in range(int(sys.stdin.readline())):
	n, m = map(int, sys.stdin.readline().split())
	array = list(map(int, sys.stdin.readline().split()))

	dp = []
	index = 0

	for i in range(n): # 2차원 DP 테이블 초기화
		dp.append(array[index:index + m])
		index += m

	for j in range(1, m):
		for i in range(n):
			if i == 0: # 왼쪽 위에서 오는 경우
				left_up = 0
			else:
				left_up = dp[i - 1][j - 1]
			if i == n - 1: # 왼쪽 아래에서 오는 경우
				left_down = 0
			else:
				left_down = dp[i + 1][j - 1]
			left = dp[i][j - 1] # 왼쪽에서 오는 경우
			dp[i][j] = dp[i][j] + max(left_up, left_down, left) # 점화식

	result = 0

	for i in range(n):
		result = max(result, dp[i][m - 1])

	print(result)
