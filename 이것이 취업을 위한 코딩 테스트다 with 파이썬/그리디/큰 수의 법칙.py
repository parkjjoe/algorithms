import sys

n, m, k = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
result = 0

number.sort()
first = number[-1] # 계산에는 오직 2개의 숫자만 번갈아가며 사용됨.
second = number[-2]

while 1: # m이 0이 될 때까지 반복
  for _ in range(k): # 가장 큰 수 k번 더하기
    if m == 0:
      break
    result += first
    m -= 1

  if m == 0:
    break
    
  result += second # 두번째로 큰 수 1번 더하기
  m -= 1

print(result)
