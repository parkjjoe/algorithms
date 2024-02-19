from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    
    if direction == "right":
        numbers.appendleft(numbers[-1])
        numbers.pop()
    else:
        numbers.append(numbers[0])
        numbers.popleft()
    return list(numbers)