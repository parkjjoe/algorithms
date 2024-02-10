import sys

def func(a, b):
    return (a + b) * (a - b)

a, b = map(int, sys.stdin.readline().split())

print(func(a, b))