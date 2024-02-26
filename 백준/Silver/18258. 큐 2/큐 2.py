import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for _ in range(n):
    order = list(map(str, sys.stdin.readline().rstrip().split()))

    if order[0] == "push":
        queue.append(int(order[1]))
    elif order[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        print(1 if not queue else 0)
    elif order[0] == "front":
        print(queue[0] if queue else -1)
    elif order[0] == "back":
        print(queue[-1] if queue else -1)