def solution(my_string, letter):
    return "".join(str(i) for i in my_string if i not in letter)