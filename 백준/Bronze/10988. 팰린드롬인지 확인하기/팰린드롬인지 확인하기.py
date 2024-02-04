import sys

s = list(str(sys.stdin.readline().rstrip()))
sr = s[::-1]

if s == sr:
    print("1")
else:
    print("0")