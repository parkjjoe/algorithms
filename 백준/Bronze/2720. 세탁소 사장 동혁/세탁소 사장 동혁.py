import sys

t = int(sys.stdin.readline())
q, d, n, p = 25, 10, 5, 1

for _ in range(t):
    c = int(sys.stdin.readline())

    print(c//q, c%q//d, c%q%d//n, c%q%d%n//p)