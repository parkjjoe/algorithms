import sys

s = str(sys.stdin.readline().rstrip())

height = 10

for i in range(len(s) - 1):
    if s[i+1] == s[i]:
        height += 5
    else:
        height += 10

print(height)