def solution(my_string):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    answer = [0] * len(alphabet)
    
    for i in my_string:
        count = my_string.count(i)
        answer[alphabet.index(i)] = count
    return answer