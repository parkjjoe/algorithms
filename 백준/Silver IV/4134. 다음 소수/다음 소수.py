import sys
import math

n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())

    while 1:
        if a == 0 or a == 1:
            print(2)
            break

        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                break
        else:
            print(a)
            break

        a += 1