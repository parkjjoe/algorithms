import sys

n = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
m = max(score)

for i in range(n):
    score[i] = score[i] / m * 100

print(sum(score) / n)