def solution(myString, pat):
    str = ""
    
    for i in myString:
        if i == "A":
            str += "B"
        else:
            str += "A"
    
    return 1 if pat in str else 0