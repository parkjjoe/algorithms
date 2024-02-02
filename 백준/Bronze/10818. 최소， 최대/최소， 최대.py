import sys

N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))

print(f"{min(n)} {max(n)}")