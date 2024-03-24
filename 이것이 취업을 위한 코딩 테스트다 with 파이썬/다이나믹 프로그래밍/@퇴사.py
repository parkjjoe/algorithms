import sys

n = int(sys.stdin.readline())
work = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [0] * (n + 1) # i일부터 마지막 날까지 낼 수 있는 최대 이익

for i in range(n - 1, -1, -1): # 리스트를 뒤에서부터 확인
	if work[i][0] + i > n: # i일에 상담하다가 퇴사일을 넘기는 경우 상담 안 함.
		dp[i] = dp[i + 1]
	else: # i일에 상담하는 것과 안 하는 것 중 큰 값 선택
		dp[i] = max(dp[i + 1], work[i][1] + dp[i + work[i][0]])

print(dp[0])
