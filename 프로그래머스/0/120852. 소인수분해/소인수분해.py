def solution(n):
    result = []
    num = 2
    
    while num <= n:
        if n % num == 0:
            result.append(num)
            n //= num
        else:
            num += 1
    return sorted(set(result))