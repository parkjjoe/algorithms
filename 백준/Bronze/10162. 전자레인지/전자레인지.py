import sys

t = int(sys.stdin.readline())

if t % 10 != 0:
    print(-1)
else:
    print(t // 300, (t % 300) // 60, ((t % 300) % 60) // 10)