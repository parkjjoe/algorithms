def solution(N, stages):
    result = []
    length = len(stages)
    
    for i in range(1, N + 1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        result.append((i, fail))
        length -= count
    
    result = sorted(result, key=lambda x: -x[1])
    
    return [i[0] for i in result]
