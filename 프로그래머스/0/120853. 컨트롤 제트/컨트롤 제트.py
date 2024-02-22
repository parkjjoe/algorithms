def solution(s):
    sum = 0
    li = [i for i in s.split()]
    
    for i in range(len(li)):
        if li[i] != "Z":
            sum += int(li[i])
        else:
            sum -= int(li[i-1])
    return sum