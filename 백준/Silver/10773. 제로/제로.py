import sys

k = int(sys.stdin.readline())

stack = []

for _ in range(k):
    a = int(sys.stdin.readline())

    stack.pop() if a == 0 else stack.append(a)

print(sum(stack))