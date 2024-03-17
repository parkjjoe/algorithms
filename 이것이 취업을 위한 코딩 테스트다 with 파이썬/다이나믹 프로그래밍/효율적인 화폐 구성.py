import sys

n, m = map(int, sys.stdin.readline().split())
array = [int(sys.stdin.readline()) for _ in range(n)]

d = [10001] * (m + 1) # m이 최대 10000이므로 10000보다 큰 값인 10001로 초기화

# 바텀업
d[0] = 0

for i in range(n):
	for j in range(array[i], m + 1):
		d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001: # m원을 만드는 방법이 없으면 -1 출력
	print(-1)
else:
	print(d[m])
