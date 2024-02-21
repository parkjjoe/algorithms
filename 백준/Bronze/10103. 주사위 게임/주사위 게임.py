import sys

n = int(sys.stdin.readline())

score = [100, 100]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if a > b:
        score[1] -= a
    elif a < b:
        score[0] -= b
    elif a == b:
        pass

print(f"{score[0]}\n{score[1]}")