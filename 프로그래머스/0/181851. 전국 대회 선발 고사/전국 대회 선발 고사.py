def solution(rank, attendance):
    students = sorted([(rank, idx) for idx, rank in enumerate(rank)])
    select = []
    
    for rank, idx in students:
        if attendance[idx]:
            select.append(idx)
        
            if len(select) == 3:
                break

    return 10000 * select[0] + 100 * select[1] + select[2]