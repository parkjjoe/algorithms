import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    order = list(map(str, sys.stdin.readline().rstrip().split()))

    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "pop":
        print(-1) if not stack else print(stack.pop())
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        print(1) if not stack else print(0)
    elif order[0] == "top":
        print(-1) if not stack else print(stack[-1])