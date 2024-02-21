import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    
    amount = {}

    for _ in range(n):
        s, l = map(str, sys.stdin.readline().rstrip().split())
        amount[s] = int(l)

    print(max(amount, key=amount.get))