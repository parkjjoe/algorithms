def solution(n):
    num = 0
    
    for _ in range(n):
        num += 1
        
        while "3" in str(num) or num % 3 == 0:
            num += 1
            
    return num