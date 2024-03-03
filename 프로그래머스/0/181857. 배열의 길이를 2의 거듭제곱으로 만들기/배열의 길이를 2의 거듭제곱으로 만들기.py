def solution(arr):
    n = 0
    
    while len(arr) != 2 ** n:
        if len(arr) == 2 ** n:
            break
            
        if len(arr) > 2 ** n:
            n += 1
        else:
            length = (2 ** n) - len(arr)
            for _ in range(length):
                arr.append(0)
    return arr