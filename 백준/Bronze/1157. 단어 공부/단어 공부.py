import sys

s = str(sys.stdin.readline().rstrip()).upper() # 입력받고 대문자 변환
ss = list(set(s)) # s에서 중복값 제거
list = []

for i in ss:
    list.append(s.count(i)) # 입력값에서 알파벳 개수 세서 list에 저장

if list.count(max(list)) > 1: # list에 저장된 최댓값 수가 2개 이상이면 ? 출력
    print("?")
else:
    print(ss[(list.index(max(list)))]) # 그렇지 않으면 list의 최댓값의 index 번호에 해당하는 알파벳을 ss에서 출력