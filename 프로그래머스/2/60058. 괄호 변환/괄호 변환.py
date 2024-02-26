# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호 개수
    
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호 개수
    
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않으면 False
                return False
            count -= 1
    return True # 쌍이 맞으면 True

def solution(p):
    answer = ''
    
    if p == '':
        return answer
    
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    
    # "올바른 괄호 문자열"이면 v에 대해 함수 수행 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    else: # "올바른 괄호 문자열"이 아니면 아래 과정 수행
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1]) # 첫 번째와 마지막 문자 제거
        
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        
        answer += "".join(u)
    return answer