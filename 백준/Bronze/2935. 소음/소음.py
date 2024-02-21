import sys

a = int(sys.stdin.readline())
s = str(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline())

print(a * b if s == "*" else a + b)