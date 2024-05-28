import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
reverse = a[::-1]

increase = [1] * n
decrease = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]: # 증가 수열
            increase[i] = max(increase[i], increase[j] + 1)

        if reverse[i] > reverse[j]: # 감소 수열
            decrease[i] = max(decrease[i], decrease[j] + 1)

decrease = decrease[::-1]

result = []
for i in range(n):
    result.append(decrease[i] + increase[i] - 1)

print(max(result))