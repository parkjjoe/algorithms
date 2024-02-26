def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if int(finished[i]) == 0:
            answer.append(todo_list[i])
    return answer