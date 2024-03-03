import sys
from math import factorial

n = int(sys.stdin.readline())

result = str(factorial(n))[::-1]

count = 0

for i in result:
    if i != "0":
        break
    else:
        count += 1

print(count)