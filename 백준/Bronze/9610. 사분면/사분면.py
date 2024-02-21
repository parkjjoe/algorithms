import sys

n = int(sys.stdin.readline())

result = [0] * 5

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if x > 0 and y > 0:
        result[0] += 1 # Q1
    elif x < 0 and y > 0:
        result[1] += 1 # Q2
    elif x < 0 and y < 0:
        result[2] += 1 # Q3
    elif x > 0 and y < 0:
        result[3] += 1 # Q4
    elif x == 0 or y == 0:
        result[4] += 1 # AXIS

print(f"Q1: {result[0]}\nQ2: {result[1]}\nQ3: {result[2]}\nQ4: {result[3]}\nAXIS: {result[4]}")