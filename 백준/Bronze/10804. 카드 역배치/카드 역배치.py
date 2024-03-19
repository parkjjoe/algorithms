import sys

card = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, sys.stdin.readline().split())
    card[a - 1:b] = card[a - 1:b][::-1]

print(*card)