import sys

s = list(str(sys.stdin.readline().rstrip()))

result = int(s[0])

for i in range(1, len(s)):
  if s[i] <= "1" or result <= 1:
    result += int(s[i])
  else:
    result *= int(s[i])

print(result)
