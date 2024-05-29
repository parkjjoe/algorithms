import sys

n = int(sys.stdin.readline())
dp = [1] * n

li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

li.sort()

for i in range(1, n):
    for j in range(i):
        if li[i][1] > li[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))