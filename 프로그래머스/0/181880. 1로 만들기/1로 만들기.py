def solution(num_list):
    total = 0
    
    for i in num_list:
        count = 0
        
        while 1:
            if i == 1:
                break
            elif i % 2 == 0:
                i //= 2
                count += 1
            elif i % 2 == 1:
                i = (i - 1) // 2
                count += 1

        total += count
    return total