import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(map(int, sys.stdin.readline().split()))

    count = 1

    while queue:
        if queue[0] < max(queue):
            queue.append(queue.popleft())
        else:
            if m == 0: break

            queue.popleft()
            count += 1

        m = m - 1 if m > 0 else len(queue) - 1

    print(count)