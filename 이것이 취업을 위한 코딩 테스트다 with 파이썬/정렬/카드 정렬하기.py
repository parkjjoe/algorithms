import sys
import heapq

n = int(sys.stdin.readline())

heap = []
result = 0

for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    total = one + two
    heapq.heappush(heap, total)

    result += total

print(result)
