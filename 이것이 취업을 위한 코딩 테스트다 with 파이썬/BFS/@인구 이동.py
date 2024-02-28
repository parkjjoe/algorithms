import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    union = []
    union.append((i, j))

    while queue:
        x, y = queue.popleft()

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0: # 옆 나라 확인해서 인구 차이가 조건에 맞으면 연합에 추가
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union

# 인구 이동이 안 될 때까지 반복
while 1:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0: # 방문하지 않은 나라가 있으면 BFS 수행
                visited[i][j] = 1
                country = bfs(i, j)

                if len(country) > 1: # 연합 나라가 2개 이상이라 인구 이동이 필요하면 flag를 1로 바꾸고 각 칸의 인구 수를 계산해 people 계산
                    flag = 1
                    people = sum(graph[x][y] for x, y in country) // len(country)

                    for x, y in country:
                        graph[x][y] = people

    if flag == 0: # flag가 0이면 인구 이동 끝
        print(result)
        break

    result += 1 # 계속 인구 이동이 일어나면 날짜 수 1 증가
