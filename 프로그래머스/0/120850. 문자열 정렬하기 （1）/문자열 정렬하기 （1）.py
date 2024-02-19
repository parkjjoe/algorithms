def solution(my_string):
    answer = []
    num = "0123456789"
    
    for i in my_string:
        if i in num:
            answer.append(int(i))
    answer.sort()
    return answer