def solution(x1, x2, x3, x4):
    x12, x34 = True, True
    
    if not x1 and not x2:
        x12 = False
    
    if not x3 and not x4:
        x34 = False
    
    return True if x12 and x34 else False