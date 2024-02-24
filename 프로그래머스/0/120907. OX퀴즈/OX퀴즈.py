def solution(quiz):
    result = []
    
    for i in quiz:
        equation = i.split(" = ")
        
        if eval(equation[0]) == int(equation[1]):
            result.append("O")
        else:
            result.append("X")
    
    return result