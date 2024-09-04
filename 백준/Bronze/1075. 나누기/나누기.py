import sys

n = int(sys.stdin.readline())
f = int(sys.stdin.readline())

n = n - (n % 100)

for i in range(100):
	if (n + i) % f == 0:
		if i < 10:
			print("0" + str(i))
		else:
			print(i)
		break