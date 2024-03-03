def solution(picture, k):
    answer = []
    
    for i in picture:
        row = ""
        
        for j in i:
            row += j * k
            
        for _ in range(k):
            answer.append(row)
    
    return answer