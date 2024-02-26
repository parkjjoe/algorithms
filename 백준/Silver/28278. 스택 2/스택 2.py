import sys

n = int(sys.stdin.readline())

stack = []
inputs = []

for _ in range(n):
    inputs = list(map(int, sys.stdin.readline().rstrip().split()))

    if inputs[0] == 1:
        stack.append(inputs[1])
    elif inputs[0] == 2:
        print(stack.pop()) if len(stack) > 0 else print(-1)
    elif inputs[0] == 3:
        print(len(stack))
    elif inputs[0] == 4:
        print(1) if len(stack) == 0 else print(0)
    elif inputs[0] == 5:
        print(stack[-1]) if len(stack) > 0 else print(-1)

    inputs.clear()