import sys

n = int(sys.stdin.readline())
coin = list(map(int, sys.stdin.readline().split()))

coin.sort()
number = 1

for i in coin:
  if number < i:  # 만들 수 없는 금액을 찾으면 끝
    break
  else:
    number += i

print(number)
