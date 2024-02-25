import sys

n = int(sys.stdin.readline())

for i in range(n):
    print("* " * n if i % 2 == 0 else " *" * n)