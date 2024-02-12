import sys

n, m = map(int, sys.stdin.readline().split())
board = []
result = []

for i in range(n):
    board.append(str(sys.stdin.readline().rstrip()))

for i in range(n-7): # 시작 지점 (0, 0) 기준 8 × 8 크기가 되어야 함.
    for j in range(m-7): # 시작 지점 (0, 0) 기준 8 × 8 크기가 되어야 함.
        white = 0 # (0, 0)이 W로 시작하는 경우, 덧칠해야 하는 횟수 계산
        black = 0 # (0, 0)이 B로 시작하는 경우, 덧칠해야 하는 횟수 계산

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0: # 짝수 인덱스인 경우 모두 같은 색이어야 함.
                    if board[k][l] != "W": # (0, 0)이 W로 시작하는 경우, 짝수 인덱스가 W가 아니면 white에 1 추가
                        white += 1
                    if board[k][l] != "B": # (0, 0)이 B로 시작하는 경우. 짝수 인덱스가 B가 아니면 black에 1 추가
                        black += 1
                else: # 홀수 인덱스인 경우에도 모두 같은 색이어야 함.
                    if board[k][l] != "B": # (0, 0)이 W로 시작하는 경우, 홀수 인덱스가 B가 아니면 white에 1 추가
                        white += 1
                    if board[k][l] != "W": # (0, 0)이 B로 시작하는 경우, 홀수 인덱스가 W가 아니면 black에 1 추가
                        black += 1

        result.append(white)
        result.append(black)

print(min(result))