import sys

n = int(sys.stdin.readline())

for _ in range(n):
    string = str(sys.stdin.readline().rstrip())
    score = 0
    total_score = 0

    for i in string:
        if i == "O":
            score += 1
            total_score += score
        else:
            score = 0

    print(total_score)