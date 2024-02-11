import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = []

for i in range(m, n+1):
    check = 0

    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0: # 나눠지는 수가 있다면 소수가 아니므로 check을 1로 변경, result에 추가되지 않음.
            check = 1

    if check == 0: # 나눠지는 수가 없다면 소수이므로 check는 그대로 0일 것이고, 이 때 result에 추가
        result.append(i)

if result == []:
    print("-1")
else:
    print(sum(result))
    print(min(result))