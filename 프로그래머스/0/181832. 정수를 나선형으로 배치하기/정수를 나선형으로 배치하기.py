def solution(n):
    if n == 1: return [[1]] # n = 1 예외처리
    
    answer = [[0 for j in range(n)] for i in range(n)]
    x, y = 0, 0
    direction = "r" # r: right > d: down > l: left > u: up > r ...
    
    for i in range(n * n):
        answer[x][y] = i + 1
        
        if direction == "r":
            y += 1
            
            if y == n - 1 or answer[x][y + 1] != 0: # 리스트 끝에 도달했거나 이미 값이 있으면 방향 전환
                direction = "d"
        elif direction == "d":
            x += 1
            if x == n - 1 or answer[x + 1][y] != 0:
                direction = "l"
        elif direction == "l":
            y -= 1
            if y == 0 or answer[x][y - 1] != 0:
                direction = "u"
        elif direction == "u":
            x -= 1
            if x == n - 1 or answer[x - 1][y] != 0:
                direction = "r"
                
    return answer