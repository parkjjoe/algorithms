import sys

score = []

for _ in range(5):
    score.append(int(sys.stdin.readline()))

for i in range(5):
    if score[i] < 40:
        score[i] = 40

print(int(sum(score) / len(score)))