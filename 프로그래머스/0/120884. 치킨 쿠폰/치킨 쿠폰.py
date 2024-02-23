def solution(chicken):
    plus_chicken = 0
    
    while chicken >= 10:
        plus_chicken += chicken // 10
        
        chicken = chicken // 10 + chicken % 10
    
    return plus_chicken