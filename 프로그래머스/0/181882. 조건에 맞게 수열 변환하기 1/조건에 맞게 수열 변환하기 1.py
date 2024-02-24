def solution(arr):
    result = []
    
    for i in arr:
        if i < 50:
            if i % 2 == 0:
                result.append(i)
            else:
                result.append(i * 2)
        else:
            if i % 2 == 0:
                result.append(i // 2)
            else:
                result.append(i)
    return result