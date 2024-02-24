def solution(num, total):
    avg = total // num
    
    return sorted(i for i in range(avg - ((num - 1) // 2), avg + ((num + 2) // 2)))