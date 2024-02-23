# 1. 특정 지점 주변 상하좌우를 살펴본 뒤 주변 지점 중 값이 0이면서 아직 방문하지 않았다면 해당 지점 방문
# 2. 방문 지점에서 다시 상하좌우를 살펴보기
# 3. 1~2번 과정을 모든 노드에 반복하여 방문하지 않은 지점의 수 세기
import sys

n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# DFS로 특정 노드 방문 후 연결된 모든 노드 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치도 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 대해 음료수 채우기
result = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
