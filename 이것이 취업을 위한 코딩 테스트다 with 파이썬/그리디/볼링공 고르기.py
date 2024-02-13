import sys

n, m = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(n - 1):
  for j in range(i + 1, n):  # 본인과 본인 이전의 숫자들과의 비교는 이미 이전 숫자들이 고려했음.
    if k[i] != k[j]:
      result += 1

print(result)
