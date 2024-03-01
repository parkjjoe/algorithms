import sys

n = int(sys.stdin.readline())

dance = set()

for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())

    if "ChongChong" == a or "ChongChong" == b or a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))