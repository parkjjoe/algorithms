def solution(strArr):
    answer = [len(i) for i in strArr]
    count = []
    
    for i in set(answer):
        count.append(answer.count(i))
    return max(count)