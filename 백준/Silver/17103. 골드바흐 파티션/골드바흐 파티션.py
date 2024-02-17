import sys

t = int(sys.stdin.readline())

sosu = [1] * 1000001
sosu[0], sosu[1] = 0, 0

for i in range(2, 1000001): # 에라토스테네스의 체
    if sosu[i]:
        for j in range(2 * i, 1000001, i): # 2의 배수 제거, 3의 배수 제거, 5의 배수 제거, ...
            sosu[j] = 0 # 소수가 아니면 0

for _ in range(t):
    n = int(sys.stdin.readline())

    count = 0

    for i in range(2, n // 2 + 1):
        if sosu[i] and sosu[n - i]: # i와 n-i가 소수이면(sosu의 인덱스 값이 1이면 소수이고 i와 n-i를 더하면 n이 된다.) count 1 증가
            count += 1

    print(count)