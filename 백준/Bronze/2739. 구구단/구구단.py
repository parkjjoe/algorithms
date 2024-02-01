import sys

a = int(sys.stdin.readline())

for i in range(1, 10):
    b = a * i
    print(f'{a} * {i} = {b}')