import sys

n = int(sys.stdin.readline())

for _ in range(n):
	a, b = map(str, sys.stdin.readline().rstrip().split())
	
	print("Impossible") if sorted(a) != sorted(b) else print("Possible")