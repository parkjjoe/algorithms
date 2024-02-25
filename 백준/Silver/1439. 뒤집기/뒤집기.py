import sys

s = str(sys.stdin.readline().rstrip())

change0 = 0
change1 = 0

if s[0] == "1":  # 첫 번째 원소가 1이면 0으로 바꾸는 경우에 + 1
  change0 += 1
else:  # 첫 번째 원소가 0이면 1로 바꾸는 경우에 + 1
  change1 += 1

for i in range(len(s) - 1):
  if s[i] != s[i + 1]:  # 현재 원소와 다음 원소의 값이 다르면
    if s[i + 1] == "1":  # 근데 다음 원소가 1이면 0으로 바꾸는 경우에 + 1
      change0 += 1
    else:  # 근데 다음 원소가 0이면 1로 바꾸는 경우에 + 1
      change1 += 1

print(min(change0, change1))