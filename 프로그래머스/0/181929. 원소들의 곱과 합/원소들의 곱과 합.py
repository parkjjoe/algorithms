def solution(num_list):
    prod, sum = 1, 0
    
    for i in num_list:
        prod *= i
        sum += i
    return 1 if prod < sum ** 2 else 0