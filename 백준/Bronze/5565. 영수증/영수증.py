import sys

cost = int(sys.stdin.readline())

for _ in range(9):
    book = int(sys.stdin.readline())
    cost -= book

print(cost)