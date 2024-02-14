import sys

n = int(sys.stdin.readline())
have = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
no_have = list(map(int, sys.stdin.readline().split()))

dict = {}

for i in have: # 가지고 있는 숫자가 dict에 있는 만큼 count
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for i in no_have: # 정수 묶음 list에서 dict에 있다면(가지고 있는 숫자라면) 그 숫자의 value 출력, 아니면 0 출력
    if i in dict:
        print(dict[i], end=" ")
    else:
        print("0", end=" ")