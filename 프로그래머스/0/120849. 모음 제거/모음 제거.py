def solution(my_string):

    return "".join(str(i) for i in my_string if i not in "aeiou")