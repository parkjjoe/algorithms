def solution(arr):
    answer = [[]]
    
    if len(arr) > len(arr[0]):
        for _ in range(len(arr) - len(arr[0])):
            for i in range(len(arr)):
                arr[i].append(0)
    else:
        for _ in range(len(arr[0]) - len(arr)):
            arr.append([0] * len(arr[0]))
    return arr