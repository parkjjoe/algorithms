import sys
from itertools import combinations

n = int(sys.stdin.readline())

graph = [] # 복도
teachers = [] # 선생님
spaces = [] # 빈 공간

for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().rstrip().split())))

    for j in range(n):
        if graph[i][j] == "T": # 선생님 위치 저장
            teachers.append((i, j))
        if graph[i][j] == "X": # 빈 공간 저장
            spaces.append((i, j))

# 감시 진행, 학생 발견 시 True
def watch(x, y, direction):
    if direction == 0: # 왼쪽 방향 감시
        while y >= 0:
            if graph[x][y] == "S": return True
            if graph[x][y] == "O": return False
            y -= 1
    if direction == 1: # 오른쪽 방향 감시
        while y < n:
            if graph[x][y] == "S": return True
            if graph[x][y] == "O": return False
            y += 1
    if direction == 2: # 위쪽 방향 감시
        while x >= 0:
            if graph[x][y] == "S": return True
            if graph[x][y] == "O": return False
            x -= 1
    if direction == 3: # 아래쪽 방향 감시
        while x < n:
            if graph[x][y] == "S": return True
            if graph[x][y] == "O": return False
            x += 1
    return False

# 벽 설치 후 학생이 감지되는지 검사
def check():
    for x, y in teachers: # 선생님 위치 확인
        for i in range(4): # 4가지 방향으로 학생이 감지되는지 확인
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 감지되지 않도록 벽 설치가 되는지의 여부

# 빈 공간에서 3개 뽑는 조합
for data in combinations(spaces, 3):
    for x, y in data: # 벽 설치해보기
        graph[x][y] = "O"
    if not check(): # 학생이 감지되지 않았으면 find = True
        find = True
        break
    for x, y in data: # 학생이 감지됐으면 벽 허물고 다시 하기
        graph[x][y] = "X"

print("YES" if find else "NO")