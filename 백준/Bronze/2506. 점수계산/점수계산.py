import sys

n = int(sys.stdin.readline())
result = list(map(int, sys.stdin.readline().split()))

score = 0
total = 0

for i in range(len(result)):

    if result[i] == 1:
        score += 1
        total += score
    elif result[i] == 0:
        score = 0

print(total)