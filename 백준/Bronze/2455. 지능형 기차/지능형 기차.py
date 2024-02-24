import sys

people = []
num = 0

for _ in range(4):
    out, ride = map(int, sys.stdin.readline().split())

    num -= out
    num += ride
    people.append(num)

print(max(people))