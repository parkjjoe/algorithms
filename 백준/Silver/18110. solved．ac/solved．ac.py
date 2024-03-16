import sys

n = int(sys.stdin.readline())

def new_round(num):
	if (num - int(num)) >= 0.5:
		return int(num) + 1
	else:
		return int(num)

if n == 0:
	print(0)
else:
	opinion = []

	for _ in range(n):
		opinion.append(int(sys.stdin.readline()))

	opinion.sort()
	cut = new_round(n * 0.15)

	print(new_round(sum(opinion[cut:n - cut]) / len(opinion[cut:n - cut])))