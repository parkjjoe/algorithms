import math

def solution(n):
    pizza = (6 * n) / math.gcd(6, n)
    return int(pizza / 6)