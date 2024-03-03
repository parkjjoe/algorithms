def solution(arr, k):
    answer = []
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
    
    if len(answer) < k:
        for _ in range(k - len(answer)):
            answer.append(-1)
    elif len(answer) > k:
        for _ in range(len(answer) - k):
            answer.pop()
    return answer