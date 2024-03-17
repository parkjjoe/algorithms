import sys

N, M, B = map(int, sys.stdin.readline().split())
minecraft = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

time = sys.maxsize
height = 0

for i in range(257):
	exceed, lack = 0, 0

	for j in range(N):
		for k in range(M):
			if minecraft[j][k] > i: # i층의 각 블럭마다 초과분, 부족분 계산
				exceed += minecraft[j][k] - i
			else:
				lack += i - minecraft[j][k]

	if exceed + B >= lack: # 초과분 + 인벤토리 블럭 수가 부족분보다 많을 때(블럭을 추가하거나 없앨 수 있는 경우)만 시간과 층수 계산
		if exceed * 2 + lack <= time:
			time = exceed * 2 + lack
			height = i

print(time, height)