import sys

n = str(sys.stdin.readline().rstrip())

front, back = 0, 0

for i in range(int(len(n) / 2)):
    front += int(n[i])

for i in range(int(len(n) / 2), len(n)):
    back += int(n[i])

if front == back:
    print("LUCKY")
else:
    print("READY")
