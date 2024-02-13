import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

group = 0
count = 0
number.sort()

for i in number:
  count += 1 # 일단 그룹에 모험가 포함시키기

  if count >= i: # 현재 그룹에 포함된 모험가의 수가 공포도보다 크면 그룹 결성
    group += 1
    count = 0 # 그룹 결성이 끝났으므로 count 초기화

print(group)
