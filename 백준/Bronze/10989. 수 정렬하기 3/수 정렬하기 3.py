import sys

n = int(sys.stdin.readline())
number = [0] * 10001

for _ in range(n):
    number[int(sys.stdin.readline())] += 1 # 입력값에 해당하는 인덱스의 값 1 증가
    # 1이 2번 입력되면, 1번 인덱스의 값이 2가 된다.

for i in range(len(number)):
    if number[i] != 0: # 인덱스의 값이 0이 아니라면, 그 인덱스의 값만큼 숫자 출력
        for _ in range(number[i]): # 1번 인덱스의 값이 2이므로, 1을 2번 출력
            print(i)