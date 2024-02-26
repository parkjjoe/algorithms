import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

graph = [] # 전체 정보
data = [] # 바이러스 정보

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

    for j in range(n):
        if graph[i][j] != 0: # 바이러스가 존재하면 data에 (바이러스 종류, 시간, x, y) 삽입
            data.append((graph[i][j], 0, i, j))

target_s, target_x, target_y = map(int, sys.stdin.readline().split())

data.sort()
q = deque(data)

# 바이러스가 퍼져나갈 수 있는 4가지 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
    virus, s, x, y = q.popleft()

    if s == target_s: # s초가 지나거나 큐가 빌 때까지 반복
        break

    # 현재 노드에서 주변 4가지 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n: # 해당 위치로 이동할 수 있는 경우
            if graph[nx][ny] == 0: # 아직 방문하지 않은 위치면 바이러스 삽입
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])