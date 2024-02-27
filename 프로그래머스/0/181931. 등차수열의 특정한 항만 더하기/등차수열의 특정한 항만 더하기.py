def solution(a, d, included):
    answer = 0
    result = []
    
    for i in range(len(included)):
        result.append(a + (d * i))
        
    for idx, v in enumerate(included):
        if v:
            answer += result[idx]
    
    return answer