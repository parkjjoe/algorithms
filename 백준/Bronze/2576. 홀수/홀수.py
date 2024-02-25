import sys

odd = []

for _ in range(7):
    a = int(sys.stdin.readline())

    if a % 2 == 1:
        odd.append(a)

if odd == []:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))