from itertools import combinations

def solution(n):
    num = []
    
    for i in range(1, n+1):
        if n % i == 0:
            num.append(i)
    
    return len(num)