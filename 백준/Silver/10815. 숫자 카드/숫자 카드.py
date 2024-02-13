import sys

n = int(sys.stdin.readline())
have = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
no_have = list(map(int, sys.stdin.readline().split()))

dict = {}

for i in range(m): # dict에 no_have(key)의 value를 0으로 초기화
    dict[no_have[i]] = 0

for i in have:
    if i in dict: # dict에 have의 원소가 있다면 value를 1로 변경
        dict[i] = 1

for i in dict:
    print(dict[i], end=" ")