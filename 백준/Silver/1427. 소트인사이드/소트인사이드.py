import sys

n = list(str(sys.stdin.readline().rstrip()))

n.sort(reverse = True)

print("".join(n))