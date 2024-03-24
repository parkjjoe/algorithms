import sys

n = int(sys.stdin.readline())

dp = []

for _ in range(n):
	dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
	for j in range(i + 1):
		if j == 0: # 왼쪽 위에서 내려오는 경우
			up_left = 0
		else:
			up_left = dp[i - 1][j - 1]
		if j == i: # 바로 위에서 내려오는 경우
			up = 0
		else:
			up = dp[i - 1][j]
		dp[i][j] = dp[i][j] + max(up_left, up) # 점화식

print(max(dp[n - 1]))