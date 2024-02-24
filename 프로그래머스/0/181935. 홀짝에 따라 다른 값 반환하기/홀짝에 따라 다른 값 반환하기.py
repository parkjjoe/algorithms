def solution(n):
    odd, even = 0, 0
    
    if n % 2 == 0:
        for i in range(0, n+1, 2):
            even += i ** 2
    else:
        for i in range(1, n+1, 2):
            odd += i
    return even if n % 2 == 0 else odd