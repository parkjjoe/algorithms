import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split())))

index = []

while queue:
    idx, num = queue.popleft()
    index.append(str(idx + 1))

    if num > 0:
        queue.rotate(-(num - 1))
    else:
        queue.rotate(-num)

print(" ".join(index))