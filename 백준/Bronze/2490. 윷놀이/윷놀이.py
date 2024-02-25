import sys

for _ in range(3):
    a = list(map(int, sys.stdin.readline().split()))

    if sum(a) == 0: print("D")
    elif sum(a) == 1: print("C")
    elif sum(a) == 2: print("B")
    elif sum(a) == 3: print("A")
    elif sum(a) == 4: print("E")