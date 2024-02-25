import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    credit = 0
    grade = 0

    for _ in range(n):
        c, g= map(float, sys.stdin.readline().split())

        credit += c
        grade += c * g

    print(int(credit), round(grade / credit, 1))