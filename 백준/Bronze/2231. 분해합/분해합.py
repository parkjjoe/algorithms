import sys

n = int(sys.stdin.readline())

for i in range(n):
    result = i + sum(map(int, str(i))) # 분해합 공식

    if result == n:
        print(i)
        break
else:
    print(0)