import sys

n = int(sys.stdin.readline())

def factorial(num):
    if num <= 1: return 1
    else:
        return factorial(num - 1) * num

print(factorial(n))