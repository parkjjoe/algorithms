import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

if a1 * n0 + a0 <= c * n0 and a1 <= c: # a1 <= c가 있어야 a가 음수여도 보장이 된다.
    print(1)
else:
    print(0)