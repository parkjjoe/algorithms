import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
dict = {}

number2 = sorted(list(set(number))) # number에서 중복값 제거 후 오름차순 정렬

for i in range(len(number2)): # number2에서 작은 값부터 번호 지정해 dict에 저장
    dict[number2[i]] = i # 입력값은 key, 그 값의 순서는 value가 됨.

for i in number: # number의 각 입력값을 dict에서 찾아 그 값(key)의 value 출력
    print(dict[i], end=" ")