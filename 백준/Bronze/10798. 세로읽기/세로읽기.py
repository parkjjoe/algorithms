import sys

word = [sys.stdin.readline().rstrip() for _ in range(5)]

for i in range(15): # 한 행에 최대 15개
    for j in range(5): # 총 5행
        if i < len(word[j]): # 어떤 행의 i번째 문자가 그 행의 길이보다 작으면 출력
            print(word[j][i], end="")