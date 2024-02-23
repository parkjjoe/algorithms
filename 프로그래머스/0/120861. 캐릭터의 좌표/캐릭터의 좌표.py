def solution(keyinput, board):
    x, y = 0, 0
    
    for i in keyinput:
        if i == "left":
            if x == -(board[0] // 2):
                pass
            else:
                x -= 1
        elif i == "right":
            if x == board[0] // 2:
                pass
            else:
                x += 1
        elif i == "up":
            if y == board[1] // 2:
                pass
            else:
                y += 1
        elif i == "down":
            if y == -(board[1] // 2):
                pass
            else:
                y -= 1
    return [x, y]