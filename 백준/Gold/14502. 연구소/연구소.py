import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 4가지 이동 방향 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 벽 세우기
def makeWall(count):
    if count == 3: # 벽 3개가 세워지면 바이러스 퍼뜨리기
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 벽을 세울 수 있으면
                graph[i][j] = 1 # 벽 세우고
                makeWall(count + 1) # count 1 증가 후 다른 벽 세우기
                graph[i][j] = 0 # 백트래킹

# 바이러스가 퍼지는 과정
def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph) # 원래의 graph는 유지

    global result
    count = 0

    # 바이러스를 큐에 삽입
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    # 4가지 방향에 대해 탐색 시작
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 바이러스가 퍼질 수 있는 경우
                if tmp_graph[nx][ny] == 0: # 해당 위치에 바이러스 배치
                    tmp_graph[nx][ny] = 2
                    queue.append((nx, ny))

    for i in range(n):
        count += tmp_graph[i].count(0)

    result = max(result, count)

makeWall(0)
print(result)