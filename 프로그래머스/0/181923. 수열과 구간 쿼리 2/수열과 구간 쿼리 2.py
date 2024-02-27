def solution(arr, queries):
    answer = []
    
    for i in queries:
        count = []
        
        for j in range(i[0], i[1] + 1):
            if arr[j] > i[2]:
                count.append(arr[j])
                
        try:   
            answer.append(min(count))
        except:
            answer.append(-1)
    return answer