import sys

n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))
count = 0

for i in number:
    check = 0

    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0: # 나눠지는 수가 있다면 소수가 아니므로 check을 1로 변경, count에 계산되지 않음.
            check = 1
    if check == 0: # 나눠지는 수가 없다면 소수이므로 check는 그대로 0일 것이고, 이 때 count 1 증가
        count += 1

print(count)