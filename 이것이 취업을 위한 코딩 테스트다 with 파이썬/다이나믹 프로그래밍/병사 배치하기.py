import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split())) # '가장 긴 증가하는 부분 수열'

array.reverse()
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘
for i in range(1, n):
	for j in range(0, i):
		if array[j] < array[i]:
			dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
