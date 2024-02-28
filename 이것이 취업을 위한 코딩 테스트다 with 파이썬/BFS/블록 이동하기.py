from collections import deque

# 특정 위치에서 이동 가능한 다음 위치 반환
def next_position(pos, board):
    next_pos = [] # 반환 결과(이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 집합에서 리스트로 변환
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]

        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0: # 이동하고자 하는 2칸이 모두 0인 경우 이동 가능
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    if pos1_x == pos2_x: # 로봇이 가로로 되어있으면 위나 아래로 회전
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 위나 아래 2칸이 모두 0인 경우 이동 가능
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    elif pos1_y == pos2_y: # 로봇이 세로로 되어있으면 좌나 우로 회전
        for i in[-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: # 좌나 우 2칸이 모두 0인 경우 이동 가능
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    return next_pos # 현재 위치에서 이동 가능한 위치 반환

def solution(board):
    # 맵 외곽에 벽 추가
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    queue = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    queue.append((pos, 0))
    visited.append(pos) # 로봇 시작 위치를 queue에 삽입 후 방문 처리

    while queue:
        pos, cost = queue.popleft()

        if (n, n) in pos: # (n, n)에 로봇이 도달하면 최단 거리 반환
            return cost

        for next_pos in next_position(pos, new_board): #현재 위치에서 이동 가능한 위치 확인
            if next_pos not in visited: # 아직 방문하지 않은 위치면 큐에 삽입 후 방문 처리
                queue.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
