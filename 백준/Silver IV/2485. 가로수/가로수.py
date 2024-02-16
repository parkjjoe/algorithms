import sys
import math

n = int(sys.stdin.readline())
tree= sorted([int(sys.stdin.readline()) for _ in range(n)])

sub = []
result = 0

for i in range(len(tree)-1):
    sub.append(abs(tree[i+1] - tree[i]))

gcd = math.gcd(*sub)

for i in sub:
    result += i // gcd - 1

print(result)