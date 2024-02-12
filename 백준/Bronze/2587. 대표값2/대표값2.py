import sys

number = []

for _ in range(5):
    number.append(int(sys.stdin.readline()))

print(int(sum(number) / 5))

number.sort()

print(number[2])