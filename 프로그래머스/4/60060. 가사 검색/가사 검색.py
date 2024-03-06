from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수 반환 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

array = [[] for _ in range(10001)] # 단어를 길이로 나눠 저장하는 리스트 (?가 단어 뒤에 나타나는 경우)
reversed_array = [[] for _ in range(10001)] # 단어를 길이로 나눠 저장 후 뒤집는 리스트 (?가 단어 앞에 나타나는 경우)

def solution(words, queries):
    answer = []
    
    for i in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(i)].append(i)
        reversed_array[len(i)].append(i[::-1])
        
    for i in range(10001): # 이진 탐색을 위해 각 단어 리스트 정렬
        array[i].sort()
        reversed_array[i].sort()
        
    for i in queries: # 쿼리를 하나씩 확인하며 처리
        if i[0] != "?": # 접미사에 와일드카드 붙은 경우
            result = count_by_range(array[len(i)], i.replace("?", "a"), i.replace("?", "z")) # ex) froaa부터 frozz까지 같은 단어의 개수 세기
        else: # 접두사에 와일드카드 붙은 경우
            result = count_by_range(reversed_array[len(i)], i[::-1].replace("?", "a"), i[::-1].replace("?", "z"))
        
        answer.append(result)
    return answer