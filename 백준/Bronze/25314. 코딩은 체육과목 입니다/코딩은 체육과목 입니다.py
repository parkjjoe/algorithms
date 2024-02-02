import sys

n = int(sys.stdin.readline())
a = n // 4
b = n % 4

if b == 0:
    print(f"{str('long ')*a}int")
else:
    print(f"{str('long ')*(a+1)}int")
