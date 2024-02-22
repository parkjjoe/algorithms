def solution(emergency):
    result = []
    
    sort_emergency = sorted(emergency, reverse=True)
    
    for i in emergency:
        result.append(sort_emergency.index(i) + 1)
    return result