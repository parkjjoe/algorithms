import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for _ in range(n):
    order = list(map(str, sys.stdin.readline().rstrip().split()))

    if order[0] == "push_front":
        queue.appendleft(order[1])
    elif order[0] == "push_back":
        queue.append(order[1])
    elif order[0] == "pop_front":
        print(-1) if not queue else print(queue.popleft())
    elif order[0] == "pop_back":
        print(-1) if not queue else print(queue.pop())
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        print(1) if not queue else print(0)
    elif order[0] == "front":
        print(-1) if not queue else print(queue[0])
    elif order[0] == "back":
        print(-1) if not queue else print(queue[-1])