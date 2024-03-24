import sys

n = int(sys.stdin.readline())

for _ in range(n):
	a, b = map(str, sys.stdin.readline().rstrip().split())

	if sorted(a) != sorted(b):
		print("Impossible")
	else:
		print("Possible")