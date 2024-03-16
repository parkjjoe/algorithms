import sys

n = int(sys.stdin.readline())

people, rank = [], []

for _ in range(n):
	weight, height = map(int, sys.stdin.readline().split())
	people.append((weight, height))

for i in people:
	count = 1

	for j in people:
		if i[0] < j[0] and i[1] < j[1]:
			count += 1

	rank.append(count)

for i in rank:
	print(i, end=" ")