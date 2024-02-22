# 현재 설치된 구조물이 가능한 구조물인지 확인
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 기둥이면
            # 바닥 위나 보의 한쪽 끝부분 위나 다른 기둥 위면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: # 설치된 것이 보라면
            # 한쪽 끝부분이 기둥 위나 양쪽 끝부분이 다른 보와 동시에 연결이면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, stuff, operate = frame
        
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제한 뒤에
            if not possible(answer): # 가능한 구조물이 아니면 재설치
                answer.append([x, y, stuff]) 
        elif operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치한 뒤에
            if not possible(answer): # 가능한 구조물이 아니면 제거
                answer.remove([x, y, stuff])

    return sorted(answer)