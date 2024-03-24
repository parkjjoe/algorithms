import sys

n = int(sys.stdin.readline())

dp = [0] * n
dp[0] = 1

i2, i3, i5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수 찾기
for i in range(1, n):
	# 가능한 곱셈 결과 중 가장 작은 수 선택
	dp[i] = min(next2, next3, next5)

	# index에 따라 곱셈 결과 증가
	if dp[i] == next2:
		i2 += 1
		next2 = dp[i2] * 2
	if dp[i] == next3:
		i3 += 1
		next3 = dp[i3] * 3
	if dp[i] == next5:
		i5 += 1
		next5 = dp[i5] * 5

print(dp[n - 1])
