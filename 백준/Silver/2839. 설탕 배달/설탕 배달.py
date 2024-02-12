import sys

n = int(sys.stdin.readline())
count = 0

while n >= 0:
    if n % 5 == 0: # n이 5로 나눠 떨어지면 바로 몫을 출력하고 끝
        count += n // 5
        print(count)
        break
    n -= 3 # n이 5로 나눠 떨어질 때까지 3kg 봉지로 걸러냄.
    count += 1
else:
    print(-1)