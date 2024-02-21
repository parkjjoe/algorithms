import sys

n = int(sys.stdin.readline())

vote = []

for _ in range(n):
    vote.append(int(sys.stdin.readline()))

print("Junhee is not cute!" if vote.count(0) > vote.count(1) else "Junhee is cute!")