import sys

n = int(sys.stdin.readline())
move = list(map(str, sys.stdin.readline().rstrip().split()))

x, y = 1, 1

for i in move:
    if i == "L" and 1 < y <= n:
        y -= 1
    elif i == "R" and 1 <= y < n:
        y += 1
    elif i == "U" and 1 < x <= n:
        x -= 1
    elif i == "D" and 1 <= x < n:
        x += 1

    if x < 1 or n < x or y < 1 or n < y:
        continue

print(x, y)
