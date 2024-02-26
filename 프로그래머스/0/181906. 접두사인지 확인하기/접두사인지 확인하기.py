def solution(my_string, is_prefix):
    answer = [my_string[:i] for i in range(len(my_string))]
    
    for i in answer:
        if i == is_prefix:
            return 1
    else:
        return 0