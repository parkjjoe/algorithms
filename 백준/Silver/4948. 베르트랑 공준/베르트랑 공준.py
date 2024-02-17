import sys
import math

sosu = [1] * (2 * 123456 + 1) # 시간 초과 해결을 위해

for i in range(2, 2 * 123456 + 1): # 미리 입력 제한 숫자까지 소수를 찾기
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0: # 소수면 1, 소수가 아니면 0
            sosu[i] = 0
            break

while 1:
    n = int(sys.stdin.readline())

    count = 0

    if n == 0:
        break

    for i in range(n + 1, 2 * n + 1):
        count += sosu[i]

    print(count)