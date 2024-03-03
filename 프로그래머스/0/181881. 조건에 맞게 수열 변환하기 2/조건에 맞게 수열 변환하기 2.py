def solution(arr):
    count = 0
    
    while 1:
        new = []
        
        for i in arr:
            if i >= 50 and i % 2 == 0:
                new.append(i // 2)
            elif i < 50 and i % 2 == 1:
                new.append(i * 2 + 1)
            else:
                new.append(i)
                
        if arr == new:
            return count
        else:
            count += 1
            arr = new