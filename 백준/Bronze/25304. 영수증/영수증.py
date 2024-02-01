import sys

total = int(sys.stdin.readline())
n = int(sys.stdin.readline())
sum = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    sum = sum + a * b

if total == sum:
    print("Yes")
else:
    print("No")