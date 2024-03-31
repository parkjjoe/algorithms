import sys

n = int(sys.stdin.readline())

c1, c2 = 0, 0
f = [0] * (n + 1)

def fib(n):
	global c1

	if n == 1 or n == 2:
		c1 += 1
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

def fibonacci(n):
	global c2
	f[1], f[2] = 1, 1

	for i in range(3, n + 1):
		c2 += 1
		f[i] = f[i - 1] + f[i - 2]
	return f[n]

fib(n)
fibonacci(n)

print(c1, c2)