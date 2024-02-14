import sys

n = int(sys.stdin.readline())

people = {} # 시간 초과로 인한 dict 사용

for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    if b == "enter":
        people[a] = True
    else:
        del people[a]

people = sorted(people.keys(), reverse = True)

for i in people:
    print(i)