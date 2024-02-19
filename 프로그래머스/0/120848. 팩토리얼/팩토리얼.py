import math

def solution(n):
    i = 10
    
    while n < math.factorial(i):
        i -= 1
    return i