def solution(myString):
    myString2 = [i if "l" < i else "l" for i in myString]
    return "".join(myString2)