def solution(score):
    answer = []
    
    for i in score:
        answer.append(sum(i) / 2)
        
    answer_sort = sorted(answer, reverse=True) # 내림차순
    
    rank = []
    
    for i in answer:
        rank.append(answer_sort.index(i) + 1)
        
    return rank