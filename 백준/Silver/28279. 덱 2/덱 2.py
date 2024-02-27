import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for _ in range(n):
    order = list(map(int, sys.stdin.readline().split()))

    if order[0] == 1:
        queue.appendleft(order[1])
    elif order[0] == 2:
        queue.append(order[1])
    elif order[0] == 3:
        print(-1 if not queue else queue.popleft())
    elif order[0] == 4:
        print(-1 if not queue else queue.pop())
    elif order[0] == 5:
        print(len(queue))
    elif order[0] == 6:
        print(1 if not queue else 0)
    elif order[0] == 7:
        print(-1 if not queue else queue[0])
    elif order[0] == 8:
        print(-1 if not queue else queue[-1])