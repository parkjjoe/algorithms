def solution(strArr):
    answer = []
    
    for i in strArr:
        if strArr.index(i) % 2 == 0:
            answer.append(i.lower())
        else:
            answer.append(i.upper())
    return answer