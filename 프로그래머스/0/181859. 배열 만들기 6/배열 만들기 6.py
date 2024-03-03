def solution(arr):
    i = 0
    stk = []
    
    while len(arr) > i:
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1
        
    return stk if stk else [-1]