import sys

t = int(sys.stdin.readline())

score = [0, 0]
for _ in range(t):
    for _ in range(9):
        y, k = map(int, sys.stdin.readline().split())
    
        score[0] += y
        score[1] += k
    
    if score[0] > score[1]:
        print("Yonsei")
    elif score[0] < score[1]:
        print("Korea")
    elif score[0] == score[1]:
        print("Draw")