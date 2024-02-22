from math import factorial

def solution(balls, share):
    return int(factorial(balls) / (factorial(balls - share) * factorial(share)))