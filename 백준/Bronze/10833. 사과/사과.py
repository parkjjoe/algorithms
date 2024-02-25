import sys

n = int(sys.stdin.readline())

count = 0

for _ in range(n):
    student, apple = map(int, sys.stdin.readline().split())

    count += apple % student

print(count)