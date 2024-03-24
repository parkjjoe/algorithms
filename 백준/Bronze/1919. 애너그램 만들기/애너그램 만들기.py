import sys

a = str(sys.stdin.readline().rstrip())
b = str(sys.stdin.readline().rstrip())

for i in b:
	if i in a:
		a = a.replace(i, "", 1)
		b = b.replace(i, "", 1)

print(len(a) + len(b))