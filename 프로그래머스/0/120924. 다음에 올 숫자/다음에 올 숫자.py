def solution(common):
    one, two, three = common[0], common[1], common[2]
    
    if two - one == three - two:
        return common[-1] + (two - one)
    
    if two // one == three // two:
        return common[-1] * (two // one)