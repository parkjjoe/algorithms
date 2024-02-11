import sys

n = int(sys.stdin.readline())

for i in range(2, n+1):
    while n % i == 0: # n이 i로 안 나눠질 때까지 반복
        if n % i == 0: # n이 i로 나눠지면 i를 출력하고 n은 i로 나눈 몫으로 변경
            print(i)
            n //= i
        else: # n이 i로 더 이상 나눠지지 않으면 i에 1를 더하고 while문 탈출
            i += 1
            break