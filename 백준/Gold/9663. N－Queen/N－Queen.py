import sys

n = int(sys.stdin.readline())

row = [0] * n
count = 0

def queen(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): # 같은 행 또는 대각선에 퀸이 있는 경우
            return True
    return False

def dfs(start):
    global count

    if start == n:
        count += 1
    else:
        for i in range(n): # 각 행이 퀸 놓기
            row[start] = i

            if not queen(start): # 퀸의 위협을 받지 않으면 탐색 이어가기
                dfs(start + 1)

dfs(0)
print(count)