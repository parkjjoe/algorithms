def solution(picture, k):
    answer = []
    
    for i in picture:
        row = ""
        
        for j in i:
            row += j * k
            
        for count in range(k):
            answer.append(row)
    
    return answer