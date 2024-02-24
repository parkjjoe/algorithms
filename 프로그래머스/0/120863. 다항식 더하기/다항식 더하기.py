def solution(polynomial):
    equation = polynomial.split(" + ")
    
    a = 0 # x 계수
    b = 0 # 상수
    
    for i in equation:
        if i.isdigit():
            b += int(i)
        else:
            if len(i) == 1:
                a += 1
            else:
                a += int(i[:-1])
                
    if str(a) == "1":
        a = ""
                
    if str(a) == "0":
        return str(b)
    elif str(b) == "0":
        return str(a) + "x"
    elif str(a) == "0" and str(b) == "0":
        return "0"
    
    return str(a) + "x + " + str(b)        